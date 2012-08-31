import settings
import parseNLM
import os
import log

class article():
	def __init__ (self, doi = None, pm = parseNLM):
		# Parser properties
		self.pm = pm
		self.filecontent = None
		
		# Data properties
		self.doi = doi
		self.xml = None
		self.doi_url = None
		self.pmid = None
		
		self.journal_id = None
		self.journal_title = None
		self.journal_issn_ppub = None
		self.journal_issn_epub = None
		self.publisher = None
		self.article_title = None
		self.abstract = None
		self.article_type = None
		self.article_institution = None
		self.article_country = None
		self.subject_area = None
		self.research_organism = None
		self.correspondence = None
		self.author_notes = None
		self.keywords = None
		self.pub_date_date = None
		self.pub_date_day = None
		self.pub_date_month = None
		self.pub_date_year = None
		self.pub_date_timestamp = None
		self.received_date_date = None
		self.received_date_day = None
		self.received_date_month = None
		self.received_date_year = None
		self.received_date_timestamp = None
		self.accepted_date_date = None
		self.accepted_date_day = None
		self.accepted_date_month = None
		self.accepted_date_year = None
		self.accepted_date_timestamp = None
		self.award_group_funding_source = None
		self.award_group_award_id = None
		self.award_group_principle_award_recipient = None
		self.funding_statement = None
		self.copyright_statement = None
		self.copyright_year = None
		self.copyright_holder = None
		self.license = None
		self.license_type = None
		self.license_url = None
		self.ack = None
		self.conflict = None
		self.citation = None

		# authors TO DO
		# refs TO DO

	def set_file_location(self, path, doc):
		document = doc.lstrip('"').rstrip('"')
		self.file_location = path + document
		
	def parse_document(self):
		self.xml = open(self.file_location)
		self.filecontent = self.pm.parse_xml(self.xml)
		
		self.doi = self.pm.doi(self.filecontent)
		self.doi_url = 'http://dx.doi.org/' + self.doi
		
		self.pmid = self.pm.pmid(self.filecontent)
		self.article_title = self.pm.article_title(self.filecontent)
		
		

def main():
	# Simple test
	a = article()
	document = "elife_pmc_preview_version_17.xml"
	a.set_file_location(settings.test_xml_path, document)
	a.parse_document()
	print a.doi

if __name__ == "__main__":
	main()