import settings
import elife_fi_test_data as elife
import fluidinfo
import urllib
import json
import logging
from time import sleep

# Configure logging to console
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch) 

# Test connection
fluidinfo.instance = settings.instance
fluidinfo.login(settings.username, settings.password)
# Object if you have one for testing already, otherwise leave blank and createObject


def main():
  # Create tags, namespaces are created automatically
  
  #createTags()
  updateValues(elife.objects)

  # Clean up by deleting tags and namespaces
  #deleteValues(elife.objects)
  #deleteTags()
  #deleteNamespaces()
  #deleteNamespace(namespace = '/' + settings.namespace)

# 1. Create object, with no about tag
def createObject():
  headers, content = fluidinfo.post('/objects')
  obj = content['id']
  return obj

def findObject(key, value):
  """
  Look for the object(s) using the key and key value
  If found, return the ids
  """
  query = settings.namespace + '/' + key + ' = "' + value + '"'
  headers, content = fluidinfo.get('/objects', query = query)

  if(len(content['ids']) > 0):
    return content['ids']
  return None
  

def createTag(tag, desc, indexed=True):
  namespace, sep, tagname = tag.rpartition('/')
  headers, content = fluidinfo.post('/tags' + namespace, body={"description": desc, "indexed": indexed, "name": tagname})
  if(int(headers['status']) == 201):
    logger.info('created tag: ' + tag)
  elif (int(headers['status']) == 412):
    logger.info('tag exists: ' + tag)
  else:
    logger.warn('unhandled HTTP status for create tag: ' + tag + ', ' + headers['status'])

def deleteTag(tag):
  headers, content = fluidinfo.delete('/tags' + tag)
  if(int(headers['status']) == 204):
    logger.info('deleted tag: ' + tag)
  elif (int(headers['status']) == 404):
    logger.info('tag did not exist: ' + tag)
  else:
    logger.warn('unhandled HTTP status for delete tag: ' + tag + ', ' + headers['status'])

def deleteNamespace(namespace):
  headers, content = fluidinfo.delete('/namespaces' + namespace)
  if(int(headers['status']) == 204):
    logger.info('deleted namespace: ' + namespace)
  elif (int(headers['status']) == 404):
    logger.info('namespace did not exist: ' + namespace)
  elif (int(headers['status']) == 412):
    logger.info('namespace was not empty, did not delete: ' + namespace)
  else:
    logger.warn('unhandled HTTP status for delete namespace: ' + namespace + ', ' + headers['status'])

def createTags():
  """ Create all tags required for the namespace.
  Does not check if they exist first before trying to create them
  """
  for t in elife.tags:
    createTag(tag = '/' + settings.namespace + '/' + t['tag'], desc=t['desc'])

def deleteTags():
  """ Delete all tags
  """
  for t in elife.tags:
    deleteTag(tag = '/' + settings.namespace + '/' + t['tag'])

def deleteNamespaces():
  """ Delete all namespaces
  """
  for t in elife.namespaces:
    deleteNamespace(namespace = '/' + settings.namespace + '/' + t['namespace'])
    
def updateValues(objects):
  # Update values of tags for the object

  for objrow in objects:
    # 1. If object ID is not specified, create one
    key = objrow['key']
    
    if(len(objrow['obj']) == 0):
      # First try to find an existing object based on a key query
      ids = findObject(key,  objrow[key])
      if(ids == None):
        obj = createObject()
        logger.info('created object: ' + obj)
      else:
        # Use the first object found
        obj = ids[0]
        logger.info('using existing object: ' + obj)
    else:
      obj = objrow['obj']
      logger.info('using existing object: ' + obj)

    # 2. Update the primary key value, doi for articles, etc.
    objpath = '/objects/' + obj + '/' + settings.namespace + '/' + key
    headers, content = fluidinfo.put(objpath, objrow[key])
    if(int(headers['status']) == 204):
      logger.info('added ' + key + ': ' + objrow[key])
    else:
      logger.warn('unhandled HTTP status for added ' + key + ': ' + objpath + ', ' + headers['status'])
      
    # Wait time: if the object id is returned, then fluidinfo is aware of the object
    #   if no object id is returned, then fluidinfo is not aware yet, and therefore
    #   wait for a little while before issuing a query based on the tag
    loop = True
    maxTries = 20
    sleepSeconds = 2
    i = 0
    while(loop == True):
      ids = findObject(key,  objrow[key])
      logger.info('checking for object: ' + objrow[key])

      if(ids == None):
        logger.info('sleeping: ' + str(sleepSeconds) + ' seconds (' + str(sleepSeconds * (i+1)) + ' sec total)' )
        sleep(sleepSeconds)
      else:
        logger.info('object found: ' + objrow[key])
        loop = False
        
      i = i+1
      if(i >= maxTries):
        loop = False

    # 3. Assuming success at this point, issue the single loader query
    headers, content = fluidinfo.put('/values', body=objrow['query'])
    if(int(headers['status']) == 204):
      logger.info('query successful on: ' + objpath + ' = ' + objrow[key])
    else:
      logger.warn('error in query on: ' + objpath + ' = ' + objrow[key])

def deleteValues(objects):
  # Delete values of tags for the object
  #  matching about/doi, and using all schema tags as those to delete
  for objrow in objects:
    key = objrow['key']
    path = settings.namespace + '/' + key + ' = "' + objrow[key] + '"'
    tags = []
    for tag in elife.tags:
      tags.append(settings.namespace + '/' + tag['tag'])

    headers, content = fluidinfo.delete('/values', query=path, tags=tags)
    if(int(headers['status']) == 204):
      logger.info('delete query successful on: ' + key + ' = ' + objrow[key])
    else:
      logger.warn('error in delete query on: ' + key + ' = ' + objrow[key])
    


# Call main, since all in one file it must be at the bottom
main()
