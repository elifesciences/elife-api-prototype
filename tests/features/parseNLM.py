from bs4 import BeautifulSoup
import cgi
import htmlentitydefs

import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/Users/ian/code/private-code/elife-api-prototype/tests/test.log')
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
	soup = BeautifulSoup(open(filelocation), "lxml")
	return soup

def extract_nodes(soup, nodename):
	tags = soup.find_all(nodename)
	return tags

def extract_first_node(soup, nodename):
	tags = extract_nodes(soup, nodename)
	tag = tags[0]
	return tag

def extract_node_text(soup, nodename):
	tag = extract_first_node(soup, nodename)
	tag_text = tag.text
	return tag_text

@revert_entities # make cleaning up the entiteis a decorator, as we may be able to drop all this code later
def title(soup):
	title_text = extract_node_text(soup, "article-title")
	return title_text