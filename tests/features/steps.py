from lettuce import *
import parseNLM as pm

import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/Users/ian/code/private-code/elife-api-prototype/tests/test.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

@step('I have the document (\S+)')
def have_the_document(step, document):
	logger.info(document)
	file_location = set_file_location(document)
	logger.info(file_location)
	world.filecontent = pm.parse_document(file_location)

@step('I get the title') 
def get_the_title(step):
	world.title = pm.title(world.filecontent)

@step('Then I see the string (.*$)')
def then_i_see_the_string(step, string):
	logger.info("about to write string")	
	logger.info(string)
	logger.info("wrote string")	
	logger.info("about to write title")	
	logger.info(world.title)
	logger.info("wrote title")	
	assert world.title == string, \
		"Got %s" % world.title 
		
def set_file_location(doc):
	document = doc.lstrip('"').rstrip('"')
	file_location = "/Users/ian/code/private-code/elife-api-prototype/sample-xml/" + document
	return file_location

	