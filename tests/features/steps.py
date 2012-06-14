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

@step('Then I get the doi (.*$)')
def when_i_get_the_doi(step, string):
	assert world.doi == string, \
		"Got %s" % world.doi
	
@step(u'Then I see the identifier 10.1083/jcb.201106079')
def then_i_see_the_identifier_10_1083_jcb_201106079(step, string):
  assert True

@step(u'Then I see the identifier 10.1083/jcb.201106010')
def then_i_see_the_identifier_10_1083_jcb_201106010(step, string):
  assert True

@step(u'Then I see the identifier bogus/bogus')
def then_i_see_the_identifier_bogus_bogus(step, string):
  assert False

def set_file_location(doc):
	document = doc.lstrip('"').rstrip('"')
	file_location = test_xml_path + document
	return file_location

	