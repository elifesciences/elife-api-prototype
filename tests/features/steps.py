from lettuce import *
import parseNLM as pm

import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/Users/ian/code/private-code/elife-api-prototype/tests/test.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

test_xml_path = "/Users/ian/code/private-code/elife-api-prototype/sample-xml/"

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
		
def set_file_location(doc):
	document = doc.lstrip('"').rstrip('"')
	file_location = test_xml_path + document
	return file_location

	