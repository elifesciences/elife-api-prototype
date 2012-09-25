from fom.session import Fluid
from fom.mapping import Namespace, Tag
from fom.mapping import Object, tag_value
import settings
import time
import calendar
import article as artcl
import json

# Fluidinfo parser

session = Fluid()
session.login(settings.username, settings.password)
session.bind()

class fi_article(Object):
	doi = tag_value(settings.namespace + '/article/doi')
	doi_url = tag_value(settings.namespace + '/article/doi_url')
	pmid = tag_value(settings.namespace + '/article/pmid')
	journal_id = tag_value(settings.namespace + '/article/journal_id')
	journal_title = tag_value(settings.namespace + '/article/journal_title')
	journal_issn_ppub = tag_value(settings.namespace + '/article/journal_issn_ppub')
	journal_issn_epub = tag_value(settings.namespace + '/article/journal_issn_epub')
	publisher = tag_value(settings.namespace + '/article/publisher')
	article_title = tag_value(settings.namespace + '/article/article_title')
	abstract = tag_value(settings.namespace + '/article/abstract')
	article_type = tag_value(settings.namespace + '/article/article_type')
	article_institution = tag_value(settings.namespace + '/article/article_institution')
	article_country = tag_value(settings.namespace + '/article/article_country')
	subject_area = tag_value(settings.namespace + '/article/subject_area')
	research_organism = tag_value(settings.namespace + '/article/research_organism')
	correspondence = tag_value(settings.namespace + '/article/correspondence')
	author_notes = tag_value(settings.namespace + '/article/author_notes')
	keywords = tag_value(settings.namespace + '/article/keywords')
	pub_date_date = tag_value(settings.namespace + '/article/pub_date_date')
	pub_date_day = tag_value(settings.namespace + '/article/pub_date_day')
	pub_date_month = tag_value(settings.namespace + '/article/pub_date_month')
	pub_date_year = tag_value(settings.namespace + '/article/pub_date_year')
	pub_date_timestamp = tag_value(settings.namespace + '/article/pub_date_timestamp')
	received_date_date = tag_value(settings.namespace + '/article/received_date_date')
	received_date_day = tag_value(settings.namespace + '/article/received_date_day')
	received_date_month = tag_value(settings.namespace + '/article/received_date_month')
	received_date_year = tag_value(settings.namespace + '/article/received_date_year')
	received_date_timestamp = tag_value(settings.namespace + '/article/received_date_timestamp')
	accepted_date_date = tag_value(settings.namespace + '/article/accepted_date_date')
	accepted_date_day = tag_value(settings.namespace + '/article/accepted_date_day')
	accepted_date_month = tag_value(settings.namespace + '/article/accepted_date_month')
	accepted_date_year = tag_value(settings.namespace + '/article/accepted_date_year')
	accepted_date_timestamp = tag_value(settings.namespace + '/article/accepted_date_timestamp')
	award_group_funding_source = tag_value(settings.namespace + '/article/award_group_funding_source')
	award_group_award_id = tag_value(settings.namespace + '/article/award_group_award_id')
	award_group_principle_award_recipient = tag_value(settings.namespace + '/article/award_group_principle_award_recipient')
	funding_statement = tag_value(settings.namespace + '/article/funding_statement')
	copyright_statement = tag_value(settings.namespace + '/article/copyright_statement')
	copyright_year = tag_value(settings.namespace + '/article/copyright_year')
	copyright_holder = tag_value(settings.namespace + '/article/copyright_holder')
	license = tag_value(settings.namespace + '/article/license')
	license_type = tag_value(settings.namespace + '/article/license_type')
	license_url = tag_value(settings.namespace + '/article/license_url')
	ack = tag_value(settings.namespace + '/article/ack')
	conflict = tag_value(settings.namespace + '/article/conflict')
	authors = tag_value(settings.namespace + '/article/authors')
	refs = tag_value(settings.namespace + '/article/refs')
	components = tag_value(settings.namespace + '/article/components')
	xml = tag_value(settings.namespace + '/article/xml')

def get_article_initial(doi):
	"""
	Bulk load initial values from an existing article object
	Return the fluiddb/id (uid) object value, and
	tag values (in initial) to populate a fom Object
	"""
	uid = None
	initial = {}
	query = settings.namespace + '/article/doi = "' + doi + '"'
	tag_list = ["*"]
	objects = Fluid.bound.values.get(query, tag_list)
	if(objects.content):
		# Parse content returned with json library to convert null values, etc.
		i = json.loads(objects.content)
		if(type(i) == dict):
			# Can only handle one object returned so far
			for key, value in i["results"]['id'].items():
				uid = key
				for k, v in value.items():
					initial[k] = {"value": v['value']}
	return uid, initial


def main():
	# Basic testing / debug during development

	# Build an article object from XML file
	document = "elife-kitchen-sink.xml"
	a = artcl.article()
	a.parse_document(settings.test_xml_path, document)
	doi = a.doi

	# Query for object by doi
	#doi = "10.7554/eLife.000536"

	# Get existing object id and initial tag values, if it exists
	uid, initial = get_article_initial(doi)

	# Build fom Object with initial values, unless no fi object found
	#  then create a new object and set the doi
	if(uid != None):
		obj = fi_article(uid = uid, initial = initial)
	else:
		obj = fi_article();
		obj.create();
		obj.doi = doi
		obj.save()

	# Test print uid
	print "UID: " + obj.uid

	# Test print tag values from fom Object cache
	"""
	for tag in obj.tag_paths:
		try:
			print obj.get_cached(tag)
		except(TypeError):
			pass
	"""

	# Modify the object and save it
	"""
	if(obj.has("doi_url")):
		obj.doi_url += '.'
	else:
		obj.doi_url = 'http://dx.doi.org/' + obj.doi
	"""
	
	# Set values of article object to fi_article object
	data = a.__dict__
	for k, v in data.items():
		# Set value
		if not(k == "filecontent" or k == "pm" or k == "xml" or k == "file_location"
					 or k == "authors" or k == "refs" or k == "components" or k == "fim"):
			print k
			if(v != None):
				setattr(obj, k, v)
				
	print obj.doi_url

	# Save changes
	obj.save()

if __name__ == "__main__":
	main()