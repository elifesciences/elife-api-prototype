from lettuce import *
import os
import log
import settings
from article import article

test_xml_path = world.basedir + os.sep +  "sample-xml" + os.sep

world.a = {}

@step('And I set the article file location')
def set_the_article_file_location(step):
	world.article = article()
	world.article.set_file_location(test_xml_path, world.document)

@step('And I use the parser (\S+)') 
def i_use_the_parser(step, parser):
	assert world.article.pm.__name__ == parser, \
		"Got %s" % world.article.pm 

@step('I parse the document') 
def parse_the_document(step):
	world.article.parse_document()
	# Save the object in world for later, keyed by DOI
	world.a[world.article.doi] = world.article

@step('The article object has the doi (.*$)')
@step('And the article object has the doi (.*$)')
def the_article_object_has_the_doi(step, string):
	assert world.article.doi == string, \
		"Got %s" % world.article.doi

@step('Given I have an article object with the doi (.*$)')
def i_have_an_article_object_with_the_doi_doi(step, doi):
	if(world.a[doi]):
	  world.article = world.a[doi]

@step('And the article has parsed an XML document')
def the_article_has_parsed_an_XML_document(step):
	assert world.article.parsed == True

@step('And the article object has the property (.*$)')
def the_article_object_has_the_property_value(step, property):
	world.property = property
	
@step('Then the article object property has the value (.*$)')
def the_article_object_property_has_the_value(step, value):
	property = eval('world.article.' + world.property)
	if (value == 'None'):
	  value = None
	assert property == value, \
		"Got %s" % property
	