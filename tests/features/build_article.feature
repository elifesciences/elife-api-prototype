Feature: Create an article object and parse XML input
	In order to use the article object
	as a script 
	I will parse the XML file
	And I will get the article DOI and other properties from the object
	
  Scenario Outline: Build an article object and read the DOI
    Given I have the document <document>
		And I set the article file location
		And I use the parser <parser>
		When I parse the document
		Then the article object has the doi <doi>
	
  Examples:
    | document                         | parser   | doi
    | elife_pmc_preview_version_17.xml | parseNLM | 10.7554/eLife.00013
    | elife-sample-jun2012.xml         | parseNLM | 10.7554/eLife.000536
    | NLM3-sample-for-elife.1.xml      | parseNLM | 10.1083/jcb.201106079
    | NLM3-sample-for-elife.2.xml      | parseNLM | 10.1083/jcb.201106010

  Scenario Outline: Check an article object properties after parsing XML
    Given I have an article object with the doi <doi>
    And the article object has the doi <doi>
		And the article object has the property <property>
		Then the article object property has the value <value>
	
  Examples:
    | doi                   | property          | value
		
    | 10.7554/eLife.000536  | doi               | 10.7554/eLife.000536
    | 10.7554/eLife.000536  | article_title     | Prophylactic Platelets in Dengue: Survey Responses Highlight Lack of an Evidence Base
		
		| 10.1083/jcb.201106079 | doi               | 10.1083/jcb.201106079
		| 10.1083/jcb.201106079 | pmid              | 21911481
		| 10.1083/jcb.201106079 | article_title     | CENP-C recruits M18BP1 to centromeres to promote CENP-A chromatin assembly

    | 10.1083/jcb.201106010 | doi               | 10.1083/jcb.201106010
    | 10.1083/jcb.201106010 | pmid              | 21911479
    | 10.1083/jcb.201106010 | article_title     | Arf6 regulates AP-1B&#x02013;dependent sorting in polarized epithelial cells
		
    | 10.7554/eLife.00013   | doi               | 10.7554/eLife.00013
    | 10.7554/eLife.00013   | doi_url           | http://dx.doi.org/10.7554/eLife.00013
    | 10.7554/eLife.00013   | pmid              | None
    | 10.7554/eLife.00013   | article_title     | Bacterial regulation of colony development in the closest living relatives of animals




		