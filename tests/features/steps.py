from lettuce import *
import parseNLM as pm
import os

import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler(os.getcwd() + os.sep + 'test.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

test_xml_path = os.getcwd() + os.sep + os.pardir + os.sep +  "sample-xml" + os.sep

@step('I have the document (\S+)')
def have_the_document(step, document):
	file_location = set_file_location(document)
	world.filecontent = pm.parse_document(file_location)

@step('I get the title') 
def get_the_title(step):
	world.title = pm.title(world.filecontent)

@step('Then I see the string (.*$)')
def then_i_see_the_string(step, string):
	assert world.title == string, \
		"Got %s" % world.title 

@step('I get the doi')
def get_the_doi(step):
	world.doi = pm.doi(world.filecontent)

@step(u'Then I see the identifier (.*$)')
def then_i_see_the_identifier(step, string):
	assert world.doi == string, \
		"Got %s" % world.doi
	
@step('I get the pmid')
def get_the_pmid(step):
	world.pmid = pm.pmid(world.filecontent)

@step(u'Then I see the number (\d+)')
def then_i_see_the_number(step, number):
	assert world.pmid == number, \
		"Got %d" % world.pmid

@step('I count the number of authors')
def count_the_number_of_authors(step):
	world.authors_count = len(pm.authors(world.filecontent))

@step(u'Then I count the total authors as (\d+)')
def then_i_count_the_total_authors_as(step, number):
	number = int(number)
	assert world.authors_count == number, \
		"Got %d" % world.authors_count

def set_file_location(doc):
	document = doc.lstrip('"').rstrip('"')
	file_location = test_xml_path + document
	return file_location

	