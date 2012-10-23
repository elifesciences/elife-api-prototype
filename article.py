import settings
import parseNLM
import parseFI
import os
import log
import json
import operator

class article():
	def __init__ (self, doi = None, pm = parseNLM, fim = parseFI):
		# Parser properties
		self.pm = pm
		self.fim = fim
		self.filecontent = None
		self.file_location = None
		
		# Data properties
		self.about = None
		self.doi = doi
		self.doi_url = None
		if(doi is not None):
			self.doi_url = 'http://dx.doi.org/' + self.doi
		self.xml = None
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

		self.authors = None
		self.refs = None
		self.components = None

	def set_file_location(self, path = None, doc = None):
		if(path == None and doc == None):
			return None
		if(path == None):
			path = ""
		document = doc.lstrip('"').rstrip('"')
		self.file_location = path + document
		
	def set_filecontent(self):
		"""
		Set the xml and filecontent from the data in the
		file at file_location
		"""
		if(self.file_location != None):
			self.xml = open(self.file_location)
			self.filecontent = self.pm.parse_xml(self.xml)
		
	def parse_document(self, path = None, doc = None):
		"""
		Parse the XML data to populate the article object,
		and set the file_location if path and doc given
		"""
		if(path != None or doc != None):
			self.set_file_location(path, doc)
			self.set_filecontent()
		elif(self.file_location != None):
			# If no path and doc supplied, but it was previously set
			#  then just parse the file content
			self.set_filecontent()
			
		# Parse the filecontent
		self.doi = self.pm.doi(self.filecontent)
		self.doi_url = 'http://dx.doi.org/' + self.doi
		
		# About tag value for an article is the DOI in URL format
		self.about = self.doi_url
		
		self.pmid = self.pm.pmid(self.filecontent)
		self.article_title = self.pm.article_title(self.filecontent)
		self.journal_id = self.pm.journal_id(self.filecontent)
		self.journal_title = self.pm.journal_title(self.filecontent)
		self.journal_issn_ppub = self.pm.journal_issn(self.filecontent, "ppub")
		self.journal_issn_epub = self.pm.journal_issn(self.filecontent, "epub")
		self.publisher = self.pm.publisher(self.filecontent)
		self.abstract = self.pm.abstract(self.filecontent)
		self.article_type = self.pm.article_type(self.filecontent)
		self.article_institution = self.pm.article_institution(self.filecontent)
		self.article_country = self.pm.article_country(self.filecontent)
		self.subject_area = self.pm.subject_area(self.filecontent)
		self.research_organism = self.pm.research_organism(self.filecontent)
		self.correspondence = self.pm.correspondence(self.filecontent)
		self.author_notes = self.pm.author_notes(self.filecontent)
		self.keywords = self.pm.keywords(self.filecontent)

		self.pub_date_date = self.pm.pub_date_date(self.filecontent)
		self.pub_date_day  = self.pm.pub_date_day(self.filecontent)
		self.pub_date_month = self.pm.pub_date_month(self.filecontent)
		self.pub_date_year = self.pm.pub_date_year(self.filecontent)
		self.pub_date_timestamp = self.pm.pub_date_timestamp(self.filecontent)
		
		self.received_date_date = self.pm.received_date_date(self.filecontent)
		self.received_date_day = self.pm.received_date_day(self.filecontent)
		self.received_date_month = self.pm.received_date_month(self.filecontent)
		self.received_date_year = self.pm.received_date_year(self.filecontent)
		self.received_date_timestamp = self.pm.received_date_timestamp(self.filecontent)
		
		self.accepted_date_date = self.pm.accepted_date_date(self.filecontent)
		self.accepted_date_day = self.pm.accepted_date_day(self.filecontent)
		self.accepted_date_month = self.pm.accepted_date_month(self.filecontent)
		self.accepted_date_year = self.pm.accepted_date_year(self.filecontent)
		self.accepted_date_timestamp = self.pm.accepted_date_timestamp(self.filecontent)
		
		
		self.award_group_funding_source = self.pm.award_group_funding_source(self.filecontent)
		self.award_group_award_id = self.pm.award_group_award_id(self.filecontent)
		self.award_group_principle_award_recipient = self.pm.award_group_principle_award_recipient(self.filecontent)
		self.funding_statement = self.pm.funding_statement(self.filecontent)
		self.copyright_statement = self.pm.copyright_statement(self.filecontent)
		self.copyright_year = self.pm.copyright_year(self.filecontent)
		self.copyright_holder = self.pm.copyright_holder(self.filecontent)

		self.license = self.pm.license(self.filecontent)
		self.license_type = self.pm.license_type(self.filecontent)
		self.license_url = self.pm.license_url(self.filecontent)
		self.ack = self.pm.ack(self.filecontent)
		self.conflict = self.pm.conflict(self.filecontent)
		
		self.authors = self.pm.authors(self.filecontent)
		self.refs = self.pm.refs(self.filecontent)
		self.components = self.pm.components(self.filecontent)
		
	def load_from_fi(self):
		"""
		Load article data from fluidinfo using the DOI as the primary identifier
		"""
		if(self.doi == None):
			 return None
		# Create a temporary fom article object, to constrain the tags we get
		tmp_obj = self.fim.fi_article();
		about, uid, initial = self.fim.get_article_initial(self.doi_url, tmp_obj)
		if(about != None):
			obj = self.fim.fi_article(about = about, uid = uid, initial = initial)
			
			# Set the about tag, which is absent from the _path_map
			setattr(self, 'about', obj.about)
			
			# _path_map of the fom Object contains fluidinfo tag to
			#  object attribute mapping - use the two pieces appropriate below
			#  to load cached data from the object
			for k, v in obj._path_map.items():
				try:
					# By using get_cached here we skip making an HTTP
					#  get for every Object attribute
					val = obj.get_cached(k)
					if type(val) in [unicode,list,dict,int,bool]:
						# Only set if it is an allowed type, to avoid class instances
						#  such as fom.mapping.UNKNOWN_VALUE
						setattr(self, v, val)
				except:
					# Attribute in fom Object does not exist
					continue
		
		# Load authors
		authors = []
		query = settings.namespace + '/author/article_doi = "' + self.doi + '"'
		fi_obj = self.fim.fi_author()
		fi_type = "fi_author"
		authors = self.load_subobjects_from_fi(query, fi_obj, fi_type)
		# Sort list by authors[x]['position']
		authors.sort(key=operator.itemgetter('position'))
		setattr(self, "authors", authors)

		# Load refs
		refs = []
		query = settings.namespace + '/ref/article_doi = "' + self.doi + '"'
		fi_obj = self.fim.fi_ref()
		fi_type = "fi_ref"
		refs = self.load_subobjects_from_fi(query, fi_obj, fi_type)
		# Sort list by refs[x]['position']
		refs.sort(key=operator.itemgetter('position'))
		setattr(self, "refs", refs)
		
		# Load components
		components = []
		query = settings.namespace + '/component/article_doi = "' + self.doi + '"'
		fi_obj = self.fim.fi_component()
		fi_type = "fi_component"
		components = self.load_subobjects_from_fi(query, fi_obj, fi_type)
		# Sort list by components[x]['position']
		components.sort(key=operator.itemgetter('position'))
		setattr(self, "components", components)

	def load_subobjects_from_fi(self, query, fi_obj, fi_type):
		"""
		Authors, refs, and components are stored in fluidinfo as separate objects
		Namespace tags are defined in the obj (fom object type)
		This has been refactored out so it can be used in general purpose to bulk load
		all objects of a type using a single HTTP query
		"""
		objects = []

		if(fi_obj != None):
			tag_list = []
			for k, v in fi_obj._path_map.items():
				tag_list.append(k)
		else:
			tag_list = ["*"]
			
		data = self.fim.values_get(query, tag_list)

		if(data.content):
			i = json.loads(data.content)
			if(type(i) == dict):
				for key, value in i["results"]['id'].items():
					(about, uid, initial) = self.fim.get_uid_and_initial(key, value)
					# Check fi_obj type - have not found a way around this non-callable object
					if(fi_type == "fi_author"):
						obj = self.fim.fi_author(about = about, uid = uid, initial = initial)
					elif(fi_type == "fi_component"):
						obj = self.fim.fi_component(about = about, uid = uid, initial = initial)
					elif(fi_type == "fi_ref"):
						obj = self.fim.fi_ref(about = about, uid = uid, initial = initial)
					
					object_values = {}
	
					# Set the about tag, which is absent from the _path_map
					try:
						object_values['about'] = obj.about
					except:
						pass
	
					for k, v in obj._path_map.items():
						try:
							val = obj.get_cached(k)
							if type(val) in [unicode,list,dict,int,bool]:
								object_values[v] = val
						except:
							continue
					objects.append(object_values)
			# All done parsing objects
		return objects

	def data(self):
		"""
		Return selected dictionary values, for debugging purposes
		Undesired items are removed before returning
		"""
		data = self.__dict__
		for k, v in data.items():
			if (k == "filecontent" or k == "pm" or k == "xml" or k == "file_location" or k == "fim"):
				# Remove value
				del data[k]
		return data

def main():
	# Simple test
	a = article()
	#document = "elife_pmc_preview_version_17.xml"
	#document = "NLM3-sample-for-elife.1.xml"
	#document = "elife-kitchen-sink.xml"
	document = "elife00013.xml"
	#document = "elife-sample-jun2012.xml"
	a.parse_document(settings.test_xml_path, document)
	
	# Second example test: load the object from fluidinfo data using fom object
	#a = article(doi = "10.7554/eLife.00013")
	#a.load_from_fi()
	
	# Debug data
	#print a.data()
	print json.dumps(a.data(), sort_keys=True, indent=4)

	
	
if __name__ == "__main__":
	main()