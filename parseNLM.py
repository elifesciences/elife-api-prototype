from bs4 import BeautifulSoup
import cgi
import htmlentitydefs
import os

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

def revert_entities(function):
	"this is the dcorator"
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

def extract_nodes(soup, nodename):
	tags = soup.find_all(nodename)
	return tags

def extract_first_node(soup, nodename):
	tags = extract_nodes(soup, nodename)
	try:
		tag = tags[0]
	except(IndexError):
		# Tag not found
		return None
	return tag

def extract_node_text(soup, nodename):
	tag = extract_first_node(soup, nodename)
	try:
		tag_text = tag.text
	except(AttributeError):
		# Tag text not found
		return None
	return tag_text

def title(soup):
	return article_title(soup)
	
@revert_entities # make cleaning up the entiteis a decorator, as we may be able to drop all this code later
def article_title(soup):
	title_text = extract_node_text(soup, "article-title")
	return title_text

def doi(soup):
	tags = extract_nodes(soup, "article-id")
	for tag in tags:
		if tag['pub-id-type'] == 'doi':
			return tag.text
		
def pmid(soup):
	tags = extract_nodes(soup, "article-id")
	for tag in tags:
		if tag['pub-id-type'] == 'pmid':
			return tag.text
		
def authors(soup):
	"""Find and return all the authors"""
	tags = extract_nodes(soup, "contrib")
	authors = []
	for tag in tags:
		if tag['contrib-type'] == 'author':
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
