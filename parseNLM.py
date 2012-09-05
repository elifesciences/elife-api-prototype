from bs4 import BeautifulSoup
import cgi
import htmlentitydefs
import os
import time
import calendar

import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler(os.getcwd() + os.sep + 'test.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)


def	swap_en_dashes(textHTMLEntities):
	title = textHTMLEntities.replace("&#8211;", "&#x02013;")#.encode('ascii', 'xmlcharrefreplace')
	return title

def unicodeToHTMLEntities(text):
    """Converts unicode to HTML entities.  For example '&' becomes '&amp;'."""
    returnText = cgi.escape(text).encode('ascii', 'xmlcharrefreplace')
    return returnText

def format_text(title_text):
	textHTMLEntities = unicodeToHTMLEntities(title_text)
	textHTMLEntitiesReverted = swap_en_dashes(textHTMLEntities)
	return textHTMLEntitiesReverted

def flatten(function):
	"""
	Convert or flatten value; if list length is zero then return None,
	if length of a list is 1, convert to a string, otherwise return
	the list as given
	"""
	def wrapper(*args, **kwargs):
		value = function(*args, **kwargs)
		if(type(value) == list and len(value) == 0):
			return None
		elif(type(value) == list and len(value) == 1):
			# If there is only one list element, return a singleton
			return value[0]
		else:
			return value
		return value
	return wrapper

def revert_entities(function):
	"this is the decorator"
	def wrapper(*args, **kwargs):
		text = function(*args, **kwargs)
		formatted_text = format_text(text)
		return formatted_text
	return wrapper

def parse_document(filelocation):
	return parse_xml(open(filelocation))

def parse_xml(xml):
	soup = BeautifulSoup(xml, "lxml")
	return soup

def extract_nodes(soup, nodename, attr = None, value = None):
	tags = soup.find_all(nodename)
	if(attr != None and value != None):
		# Further refine nodes by attributes
		tags_by_value = []
		for tag in tags:
			try:
				if tag[attr] == value:
					tags_by_value.append(tag)
			except KeyError:
				continue
		return tags_by_value
	return tags

def extract_first_node(soup, nodename):
	tags = extract_nodes(soup, nodename)
	try:
		tag = tags[0]
	except(IndexError):
		# Tag not found
		return None
	return tag

def extract_node_text(soup, nodename, attr = None, value = None):
	"""
	Extract node text by nodename, unless attr is supplied
	If attr and value is specified, find all the nodes and search
	  by attr and value for the first node
	"""
	tag_text = None
	if(attr == None):
		tag = extract_first_node(soup, nodename)
		try:
			tag_text = tag.text
		except(AttributeError):
			# Tag text not found
			return None
	else:
		tags = extract_nodes(soup, nodename, attr, value)
		for tag in tags:
			try:
				if tag[attr] == value:
					tag_text = tag.text
			except KeyError:
				continue
	return tag_text

def title(soup):
	return article_title(soup)
	
@revert_entities # make cleaning up the entiteis a decorator, as we may be able to drop all this code later
def article_title(soup):
	title_text = extract_node_text(soup, "article-title")
	return title_text

def doi(soup):
	doi = extract_node_text(soup, "article-id", attr = "pub-id-type", value = "doi")
	return doi
		
def pmid(soup):
	pmid = extract_node_text(soup, "article-id", attr = "pub-id-type", value = "pmid")
	return pmid
		
def authors(soup):
	"""Find and return all the authors"""
	tags = extract_nodes(soup, "contrib", attr = "contrib-type", value = "author")
	authors = []
	for tag in tags:
		authors.append(tag)
	return authors

def references(soup):
	"""Find and return all the references"""
	references = extract_nodes(soup, "ref")
	return references

def get_references_by(soup, year = 0, source = ''):
	"""Get references by attributes, boolean 'or' match"""
	refs = []
	if(int(year) > 0):
		for ref in references(soup):
			if int(extract_node_text(ref, "year")) == int(year):
				refs.append(ref)
	if(source != ''):
		for ref in references(soup):
			try:
				if extract_node_text(ref, "source") == source:
					refs.append(ref)
			except(TypeError):
			  # Possibly no tag found and returned None
				pass
	# Return with no duplicates
	return list(set(refs))
	
def journal_id(soup):
	"""Find and return the primary journal id"""
	journal_id = extract_node_text(soup, "journal-ids", attr = "journal-id-type", value = "hwp")
	return journal_id

def journal_title(soup):
	"""Find and return the journal title"""
	journal_title = extract_node_text(soup, "journal-title")
	return journal_title

def journal_issn(soup, pub_type = None):
	"""
	Find and return the journal ISSN
	typical pub_type values: ppub, epub
	"""
	if (pub_type == None):
		return None
	journal_issn = extract_node_text(soup, "issn", attr = "pub-type", value = pub_type)
	return journal_issn

def publisher(soup):
	publisher = extract_node_text(soup, "publisher-name")
	return publisher

def abstract(soup):
	abstract = extract_node_text(soup, "abstract")
	return abstract

@flatten
def article_type(soup):
	"""
	Find the article_type from the subject values, of which
	some articles may have more than one
	"""
	article_type = []
	try:
		article_meta = extract_nodes(soup, "article-meta")
		article_categories = extract_nodes(article_meta[0], "article-categories")
		subj_group = extract_nodes(article_meta[0], "subj-group")
		tags = extract_nodes(subj_group[0], "subject")
		for tag in tags:
			article_type.append(tag.text)
	except(IndexError):
		# Tag not found
		return None
	
	return article_type

def get_article_meta_aff(soup):
	"""
	Find the aff tag in the article-meta
	that is not part of an author contrib-group
	for populating article_institution and article_country
	"""
	aff = None
	try:
		article_meta = extract_nodes(soup, "article-meta")
		aff = extract_nodes(article_meta[0], "aff")
	except(IndexError):
		# Tag not found
		return None
	return aff
	
def article_institution(soup):
	"""
	Find the article_institution from an aff tag in the article-meta
	that is not part of an author contrib-group
	"""
	article_institution = None

	aff = get_article_meta_aff(soup)
	for tag in aff:
		# Only look at the first aff tag that is not part of a contrib-group
		if (tag.parent.name != "contrib-group"):
			article_institution = extract_node_text(tag, "institution")
	return article_institution

def article_country(soup):
	"""
	Find the article_country from an aff tag in the article-meta
	that is not part of an author contrib-group
	"""
	article_country = None

	aff = get_article_meta_aff(soup)
	for tag in aff:
		# Only look at the first aff tag that is not part of a contrib-group
		if (tag.parent.name != "contrib-group"):
			article_country = extract_node_text(tag, "country")
	return article_country

def get_kwd_group(soup):
	"""
	Find the kwd-group sections for further analysis to find
	subject_area, research_organism, and keywords
	"""
	kwd_group = None
	kwd_group = extract_nodes(soup, 'kwd-group')
	return kwd_group

def subject_area(soup):
	"""
	Find the major-subject-area from the set of kwd-group tags
	"""
	subject_area = None
	kwd_group = get_kwd_group(soup)
	for tag in kwd_group:
		try:
			if(tag["kwd-group-type"] == "major-subject-area"):
				subject_area = extract_node_text(tag, "kwd")
		except KeyError:
			continue
	return subject_area

@flatten
def research_organism(soup):
	"""
	Find the research-organism from the set of kwd-group tags
	"""
	research_organism = None
	kwd_group = get_kwd_group(soup)
	for tag in kwd_group:
		try:
			if(tag["kwd-group-type"] == "research-organism"):
				research_organism = extract_node_text(tag, "kwd")
		except KeyError:
			continue
	return research_organism

@flatten
def keywords(soup):
	"""
	Find the keywords from the set of kwd-group tags
	"""
	keywords = []
	kwd_group = get_kwd_group(soup)
	for tag in kwd_group:
		try:
			if(tag["kwd-group-type"] != None):
				# A tag attribute found, skip it
				continue
		except KeyError:
			# Tag attribute not found, we want this tag value
			kwd = extract_nodes(tag, "kwd")
			for k in kwd:
				keywords.append(k.text)
	return keywords

def correspondence(soup):
	"""
	Find the corresp tags included in author-notes
	for primary correspondence
	"""
	correspondence = None
	try:
		author_notes = extract_nodes(soup, "author-notes")
		correspondence = extract_node_text(author_notes[0], "corresp")
	except(IndexError):
		# Tag not found
		return None
	return correspondence

@flatten
def author_notes(soup):
	"""
	Find the fn tags included in author-notes
	"""
	author_notes = []
	try:
		author_notes_section = extract_nodes(soup, "author-notes")
		fn = extract_nodes(author_notes_section[0], "fn")
		for f in fn:
			author_notes.append(f.text)
	except(IndexError):
		# Tag not found
		return None
	return author_notes

def get_ymd(soup):
	"""
	Get the year, month and day from child tags
	"""
	day = extract_node_text(soup, "day")
	month = extract_node_text(soup, "month")
	year = extract_node_text(soup, "year")
	return (day, month, year)

def get_pub_date(soup, pub_type = "ppub"):
	"""
	Find the publishing date for populating
	pub_date_date, pub_date_day, pub_date_month, pub_date_year, pub_date_timestamp
	Default pub_type is ppub, but will revert to epub if tag is not found
	"""
	tz = "UTC"
	
	try:
		pub_date_section = extract_nodes(soup, "pub-date", attr = "pub-type", value = pub_type)
		if(len(pub_date_section) == 0):
			if(pub_type == "ppub"):
				pub_type = "epub"
			pub_date_section = extract_nodes(soup, "pub-date", attr = "pub-type", value = pub_type)
		(day, month, year) = get_ymd(pub_date_section[0])

	except(IndexError):
		# Tag not found, try the other
		return None
	return time.strptime(year + "-" + month + "-" + day + " " + tz, "%Y-%m-%d %Z")

def pub_date_date(soup):
	"""
	Find the publishing date pub_date_date in human readable form
	"""
	pub_date = get_pub_date(soup)
	return time.strftime("%B %d, %Y", pub_date)
	
def pub_date_day(soup):
	"""
	Find the publishing date pub_date_day
	"""
	pub_date = get_pub_date(soup)
	return time.strftime("%d", pub_date)

def pub_date_month(soup):
	"""
	Find the publishing date pub_date_day
	"""
	pub_date = get_pub_date(soup)
	return time.strftime("%m", pub_date)
	
def pub_date_year(soup):
	"""
	Find the publishing date pub_date_day
	"""
	pub_date = get_pub_date(soup)
	return time.strftime("%Y", pub_date)

def pub_date_timestamp(soup):
	"""
	Find the publishing date pub_date_timestamp, in UTC time
	"""
	pub_date = get_pub_date(soup)
	return calendar.timegm(pub_date)

def get_history_date(soup, date_type = None):
	"""
	Find a date in the history tag for the specific date_type
	typical date_type values: received, accepted
	"""
	if(date_type == None):
		return None
	
	tz = "UTC"
	
	try:
		history_section = extract_nodes(soup, "history")
		history_date_section = extract_nodes(soup, "date", attr = "date-type", value = date_type)
		(day, month, year) = get_ymd(history_date_section[0])
	except(IndexError):
		# Tag not found, try the other
		return None
	return time.strptime(year + "-" + month + "-" + day + " " + tz, "%Y-%m-%d %Z")

def received_date_date(soup):
	"""
	Find the received date received_date_date in human readable form
	"""
	received_date = get_history_date(soup, date_type = "received")
	return time.strftime("%B %d, %Y", received_date)

def received_date_day(soup):
	"""
	Find the received date received_date_day
	"""
	received_date = get_history_date(soup, date_type = "received")
	return time.strftime("%d", received_date)

def received_date_month(soup):
	"""
	Find the received date received_date_day
	"""
	received_date = get_history_date(soup, date_type = "received")
	return time.strftime("%m", received_date)
	
def received_date_year(soup):
	"""
	Find the received date received_date_day
	"""
	received_date = get_history_date(soup, date_type = "received")
	return time.strftime("%Y", received_date)

def received_date_timestamp(soup):
	"""
	Find the received date received_date_timestamp, in UTC time
	"""
	received_date = get_history_date(soup, date_type = "received")
	return calendar.timegm(received_date)
	
def accepted_date_date(soup):
	"""
	Find the accepted date accepted_date_date in human readable form
	"""
	accepted_date = get_history_date(soup, date_type = "accepted")
	return time.strftime("%B %d, %Y", accepted_date)

def accepted_date_day(soup):
	"""
	Find the accepted date accepted_date_day
	"""
	accepted_date = get_history_date(soup, date_type = "accepted")
	return time.strftime("%d", accepted_date)

def accepted_date_month(soup):
	"""
	Find the accepted date accepted_date_day
	"""
	accepted_date = get_history_date(soup, date_type = "accepted")
	return time.strftime("%m", accepted_date)
	
def accepted_date_year(soup):
	"""
	Find the accepted date accepted_date_day
	"""
	accepted_date = get_history_date(soup, date_type = "accepted")
	return time.strftime("%Y", accepted_date)

def accepted_date_timestamp(soup):
	"""
	Find the accepted date accepted_date_timestamp, in UTC time
	"""
	accepted_date = get_history_date(soup, date_type = "accepted")
	return calendar.timegm(accepted_date)

def get_funding_group(soup):
	"""
	Get the funding-group sections for populating
	funding_source lists
	"""
	funding_group_section = extract_nodes(soup, "funding-group")
	return funding_group_section

@flatten
def award_group_funding_source(soup):
	"""
	Find the award group funding sources, one for each
	item found in the get_funding_group section
	"""
	award_group_funding_source = []
	funding_group_section = get_funding_group(soup)
	for fg in funding_group_section:
		funding_source = extract_node_text(fg, "funding-source")
		award_group_funding_source.append(funding_source)
	return award_group_funding_source

@flatten
def award_group_award_id(soup):
	"""
	Find the award group award id, one for each
	item found in the get_funding_group section
	"""
	award_group_award_id = []
	funding_group_section = get_funding_group(soup)
	for fg in funding_group_section:
		award_id = extract_node_text(fg, "award-id")
		award_group_award_id.append(award_id)
	return award_group_award_id

@flatten
def award_group_principle_award_recipient(soup):
	"""
	Find the award group principle award recipient, one for each
	item found in the get_funding_group section
	"""
	award_group_principle_award_recipient = []
	funding_group_section = get_funding_group(soup)
	for fg in funding_group_section:
		principal_award_recipient_text = ""
		principal_award_recipient = extract_nodes(fg, "principal-award-recipient")
		try:
			institution = extract_node_text(principal_award_recipient[0], "institution")
			surname = extract_node_text(principal_award_recipient[0], "surname")
			given_names = extract_node_text(principal_award_recipient[0], "given-names")
			# Concatenate name and institution values if found
			#  while filtering out excess whitespace
			if(given_names):
				principal_award_recipient_text += given_names
			if(principal_award_recipient_text != ""):
				principal_award_recipient_text += " "
			if(surname):
				principal_award_recipient_text += surname
			if(institution and len(institution) > 1):
				if(principal_award_recipient_text != ""):
					principal_award_recipient_text += ", "
				principal_award_recipient_text += institution
		except IndexError:
			continue
		award_group_principle_award_recipient.append(principal_award_recipient_text)
	return award_group_principle_award_recipient

def funding_statement(soup):
	"""
	Find the funding statement (one expected)
	"""
	funding_statement = None
	funding_statement = extract_node_text(soup, "funding-statement")
	return funding_statement

def get_permissions_section(soup):
	"""
	Get the permissions section for populating
	copyright and license data
	"""
	permissions_section = None
	permissions_section = extract_nodes(soup, "permissions")
	return permissions_section

def copyright_statement(soup):
	"""
	Find the copyright statement
	"""
	copyright_statement = None
	try:
		permissions_section = get_permissions_section(soup)
		copyright_statement = extract_node_text(permissions_section[0], "copyright-statement")
	except(IndexError):
		return None
	return copyright_statement

def copyright_year(soup):
	"""
	Find the copyright year
	"""
	copyright_year = None
	try:
		permissions_section = get_permissions_section(soup)
		copyright_year = extract_node_text(permissions_section[0], "copyright-year")
	except(IndexError):
		return None
	return copyright_year

def copyright_holder(soup):
	"""
	Find the copyright holder
	"""
	copyright_holder = None
	try:
		permissions_section = get_permissions_section(soup)
		copyright_holder = extract_node_text(permissions_section[0], "copyright-holder")
	except(IndexError):
		return None
	return copyright_holder

def get_license_section(soup):
	"""
	Find the license section, containing the
	license, license-url and license-type
	"""
	license_section = None
	try:
		permissions_section = get_permissions_section(soup)
		license_section = extract_nodes(permissions_section[0], "license")
	except(IndexError):
		return None
	return license_section

def license(soup):
	"""
	Find the license text
	"""
	license = None
	try:
		license_section = get_license_section(soup)
		license = extract_node_text(license_section[0], "license-p")
	except(IndexError):
		return None
	return license

def license_type(soup):
	"""
	Find the license type attribute of the license tag
	"""
	license_type = None
	try:
		license_section = get_license_section(soup)
		license_type = license_section[0]["license-type"]
	except(IndexError):
		return None
	return license_type

def license_url(soup):
	"""
	Find the license url attribute of the license tag
	"""
	license_url = None
	try:
		license_section = get_license_section(soup)
		license_url = license_section[0]["xlink:href"]
	except(IndexError):
		return None
	return license_url

def ack(soup):
	"""
	Find the acknowledgements in the ack tag
	"""
	ack = None
	ack = extract_node_text(soup, "ack")
	return ack

def conflict(soup):
	"""
	Find the conflict notes in footnote tag
	"""
	conflict = None
	try:
		conflict = extract_node_text(soup, "fn", attr = "fn-type", value = "conflict")
	except KeyError:
		return None
	return conflict