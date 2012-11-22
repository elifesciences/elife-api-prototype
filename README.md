# Prototype for an eLife API.

This eLife API code performs the following:

* Read NLM 3.0 XML (tested for eLife XML) into a Python object named `article`
* Write an `article` to [Fluidinfo][fi]
* Read from Fluidinfo data into an `article` object, when supplied a DOI

The quickstart below demonstrates how to use it.

Project discsussion is happening on Basecamp at https://basecamp.com/1860005/projects/520904-elifesciences-api

[fi]: https://fluidinfo.com/

# Project dependencies

[Beautiful soup][bs], install via
  
    $ pip install beautifulsoup4
	
lxml for robust xml parsing
  
    $ pip install lxml

fom for using Fluidinfo Objects
  
    $ pip install fom

[Lettuce][let] for testing.
	
    $ pip install lettuce
	
[bs]: http://www.crummy.com/software/BeautifulSoup/
[let]: http://packages.python.org/lettuce/

# Quickstart

## Initial configuration

1. Resave the `settings-example.py` file as `settings.py`
2. [Create a Fluidinfo account][fi-new].
3. Enter your Fluidinfo username and password into `settings.py`.
4. The namespace of `elifesciences.org/api_v1` can remain if only using read-only access to eLife's Fluidinfo API, version 1. If you want to write to Fluidinfo, you will need to specify a Fluidinfo namespace for which you have write access.

[fi-new]: https://fluidinfo.com/accounts/new/

## Loader

The basic command-line loader `load_article.py` contains logic for basic input and output.

## Parse XML

To parse XML and print out a JSON representation of an `article` object, using a sample XML file provided:

    $ python load_article.py -i sample-xml/elife00013.xml -o article
    
Parsing XML alone does not require valid Fluidinfo account username and password in the settings file. More eLife XML files can be downloaded from the [elife-articles][art] Github repository.

[art]: https://github.com/elifesciences/elife-articles

## Read from Fluidinfo

To read Fluidinfo objects and print out a JSON representation of an `article` object, you must specify a valid DOI stored in Fluidinfo, for example:

    $ python load_article.py -i fluidinfo -d "10.7554/eLife.00013" -o article
    
The `namespace` specified in the `settings.py` file will be the base namespace to search for eLife API schemas. The DOI is case-sensitive. It may take some time to find all associated Fluidinfo objects and assemble the results (10 to 15 seconds).

## Write to Fluidinfo

The necessary namespaces and tags to represent eLife API article data will be created automatically in your Fluidinfo namespace upon first using this procedure.

In the example below, parse XML and write data to Fluidinfo.

    $ python load_article.py -i sample-xml/elife00013.xml -o fluidinfo
    
This will print details about the objects found or created as part of the process. For example, loading eLife00270.xml,

    $ python load_article.py -i sample-xml/elife00270.xml -o fluidinfo
    http://dx.doi.org/10.7554/eLife.00270
    article UID: 0c0e0ea4-1530-441a-bb97-9d26ebf65647
    http://dx.doi.org/10.7554/eLife.00270
    author UID: 8d246784-5085-4187-bd5c-0aa2c6341948
    author UID: 72679377-8c6c-4d5a-b597-0dd4f133948b
    author UID: cbe5d2dd-f70e-46a4-a11c-72e25d7310e4
    author UID: a40ecf2a-02f4-4df5-8b2c-f83096bf3e84


Please keep in mind, if your namespace is readable to all users, the tags you added will be attached to the live eLife API objects. To test this function using eLife XML, you may want to set your namespace as private.

# License

[The MIT License (MIT)][mit]

[mit]: http://opensource.org/licenses/mit-license.php