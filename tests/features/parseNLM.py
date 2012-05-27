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


def swap_en_dashes(text):
	title = text.replace("&#8211;", "&#x02013;")#.encode('ascii', 'xmlcharrefreplace')
	return title

def unicodeToHTMLEntities(text):
    """Converts unicode to HTML entities.  For example '&' becomes '&amp;'."""
    returnText = cgi.escape(text).encode('ascii', 'xmlcharrefreplace')
    return returnText

def format_text(title_text):
	textHTMLEntities = unicodeToHTMLEntities(title_text)
	textHTMLEntitiesReverted = swap_en_dashes(textHTMLEntities)
	return '"' + textHTMLEntitiesReverted + '"'

def parse_document(filelocation):
	soup = BeautifulSoup(open(filelocation), "lxml")
	return soup

def extract_title_text(filesoup):
	title_tag = filesoup.find_all("article-title")[0]
	title_tag_text = title_tag.text
	return title_tag_text
	
def title(filesoup):
	title_text = extract_title_text(filesoup)
	formatted_text = format_text(title_text)
	return formatted_text 