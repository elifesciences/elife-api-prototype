import sys
import getopt
import settings
import json
import article
import parseFI as fim

def load_article(document = None):
	# Build an article object from XML file
	if document is None:
		document = "elife00013.xml"
	a = article.article()
	a.parse_document(settings.test_xml_path, document)
	return a
	
def load_article_into_fi(a = None):
	"""
	Take an article object and put values into fluidinfo
	as defined in the fom objects (fi_article, fi_author, fi_ref, fi_component)
	"""
	doi = a.doi

	# Get existing object id and initial tag values, if it exists
	tmp_obj = fim.fi_article();
	doi_url = a.doi_url
	about, uid, initial = fim.get_article_initial(doi_url, tmp_obj)
	print about
	# Build fom Object with initial values, unless no fi object found
	#  then create a new object and set the doi
	if(about != None):
		obj = fim.fi_article(about = about, uid = uid, initial = initial)
	else:
		about = a.doi_url
		obj = fim.fi_article();
		obj.create(about = about);
		obj.doi = doi
		obj.save()

	# Test print uid
	print "article UID: " + obj.uid

	# Set values of article object to fi_article object
	data = a.__dict__
	for k, v in data.items():
		# Set value
		if(k == "authors"):
			# Authors multi-dimensional array, flatten to one informational list
			authors = []
			for auth in v:
				try:
					authors.append(auth["author"])
				except(KeyError):
					continue
			if(len(authors)>0):
				setattr(obj, k, authors)

		elif(k == "refs"):
			# Refs multi-dimensional array, flatten to one informational list
			refs = []
			for ref in v:
				try:
					refs.append(ref["ref"])
				except(KeyError):
					continue
			if(len(refs)>0):
				setattr(obj, k, refs)
				
		elif(k == "components"):
			# Components multi-dimensional array, flatten to one informational list
			components = []
			for comp in v:
				try:
					components.append(comp["doi_url"])
				except(KeyError):
					continue
			if(len(components)>0):
				setattr(obj, k, components)
			
		elif not(k == "filecontent" or k == "pm" or k == "xml" or k == "file_location"
					 or k == "authors" or k == "refs" or k == "components" or k == "fim"):
			#print k
			if(v != None):
				setattr(obj, k, v)
				
	print obj.doi_url

	# Save changes to fi_article
	obj.save()
	
	# Refs

	for ref in a.refs:
		"""
		For each article reference, query fluidinfo for an exisitng object
		based on the article_doi and reference position
		Use the existing object, or create a new object
		Update values and safe it, then continue loop for all references
		"""
		article_doi = ref["article_doi"]
		position = ref["position"]
		
		tmp_obj = fim.fi_ref();
		about, uid, initial = fim.get_ref_initial(article_doi, position, tmp_obj)

		# Build fom Object with initial values, unless no fi object found
		#  then create a new object and set the doi
		if(uid != None):
			obj = fim.fi_ref(about = about, uid = uid, initial = initial)
		else:
			about = 'ref' + '_' + str(position) + '_' + article_doi + '"'
			obj = fim.fi_ref();
			obj.create(about = about);
			obj.article_doi = article_doi
			obj.position = position
			obj.save()
			
		# Test print uid
		print "ref UID: " + obj.uid
			
		for k, v in ref.items():
			setattr(obj, k, v)

		obj.save()
		
	for component in a.components:
		"""
		For each article component, query fluidinfo for an exisitng object
		based on the article_doi and component doi
		Use the existing object, or create a new object
		Update values and safe it, then continue loop for all components
		"""
		article_doi = component["article_doi"]
		component_doi = component["doi"]
		
		tmp_obj = fim.fi_component();
		about, uid, initial = fim.get_component_initial(article_doi, component_doi, tmp_obj)

		# Build fom Object with initial values, unless no fi object found
		#  then create a new object and set the doi
		if(uid != None):
			obj = fim.fi_component(about = about, uid = uid, initial = initial)
		else:
			about = component_doi
			obj = fim.fi_component();
			obj.create(about = about);
			obj.article_doi = article_doi
			obj.doi = component_doi
			obj.save()
			
		# Test print uid
		print "component UID: " + obj.uid
			
		for k, v in component.items():
			setattr(obj, k, v)

		obj.save()
		
	for author in a.authors:
		"""
		For each article author, query fluidinfo for an exisitng object
		based on the article_doi and author position
		Use the existing object, or create a new object
		Update values and safe it, then continue loop for all authors
		"""
		article_doi = author["article_doi"]
		position = author["position"]
		
		tmp_obj = fim.fi_author();
		about, uid, initial = fim.get_author_initial(article_doi, position, tmp_obj)

		# Build fom Object with initial values, unless no fi object found
		#  then create a new object and set the doi
		if(uid != None):
			obj = fim.fi_author(about = about, uid = uid, initial = initial)
		else:
			about = 'author' + '_' + str(position) + '_' + article_doi + '"'
			obj = fim.fi_author();
			obj.create(about = about);
			obj.article_doi = article_doi
			obj.position = position
			obj.save()
			
		# Test print uid
		print "author UID: " + obj.uid
			
		for k, v in author.items():
			setattr(obj, k, v)

		obj.save()
		



				
class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def main(argv=None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "hi:o:d:", ["help","in=","out=","doi="])
		except getopt.error, msg:
			raise Usage(msg)
		# more code, unchanged
	except Usage, err:
		print >>sys.stderr, err.msg
		print >>sys.stderr, "for help use --help"
		return 2
	
	input = None
	output = None
	doi = None

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print 'load_article.py -i <document | fluidinfo> -o <article | fluidinfo> -d <doi>'
			sys.exit()
		elif opt in ("-i", "--in"):
			input = arg
		elif opt in ("-o", "--out"):
			output = arg
		elif opt in ("-d", "--doi"):
			doi = arg
			
	#print 'Input format is "', input
	#print 'Output format is "', output
	#print 'DOI is "', doi
	
	if(input == "fluidinfo" and doi != None):
		a = article.article(doi)
		a.load_from_fi()
		if(output == "article"):
			# Test output
			print json.dumps(a.data(), sort_keys=True, indent=4)
			
		elif(output == "fluidinfo"):
			# In from fluidinfo, out to fluidinfo (not recommended except for testing purposes)
			load_article_into_fi(a)
		
	elif(input != "fluidinfo"):
		# Presumably a document name provided
		a = load_article(input)
		if(output == "article"):
			# Test output
			print json.dumps(a.data(), sort_keys=True, indent=4)
			
		elif(output == "fluidinfo"):
			# Update article at fluidinfo
			load_article_into_fi(a)

				
				
if __name__ == "__main__":
	main()