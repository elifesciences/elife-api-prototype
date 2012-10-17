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
    | elife00013.xml                   | parseNLM | 10.7554/eLife.00013
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
    | 10.7554/eLife.00013   | article_title     | A bacterial sulfonolipid triggers multicellular development in the closest living relatives of animals
		
    | 10.7554/eLife.00013   | article_institution  | None
    | 10.1083/jcb.201106079 | article_institution  | Department of Biochemistry, Stanford University Medical School, Stanford, CA 94305

		| 10.7554/eLife.00013   | article_type   | research-article
		| 10.1083/jcb.201106079 | article_type   | research-article
		
    | 10.7554/eLife.00013   | pub_date_date  | October 15, 2012
    | 10.1083/jcb.201106079 | pub_date_date  | September 19, 2011
		| 10.7554/eLife.000536  | pub_date_date  | June 26, 2012
		
    | 10.7554/eLife.00013   | authors[5]['surname'] | Fairclough
    | 10.7554/eLife.00013   | refs[0]['year']       | 1992
		
  Scenario Outline: Check an article object property list length after parsing XML
    Given I have an article object with the doi <doi>
    And the article object has the doi <doi>
		And the article object has the property <property>
		Then the article object property has the total length <length>
	
  Examples:
    | doi                   | property          | length
		
    | 10.7554/eLife.00013   | author_notes      | 1
    | 10.1083/jcb.201106079 | author_notes      | 1
    | 10.7554/eLife.000536  | author_notes      | 1
		
    | 10.7554/eLife.00013   | keywords          | 4
    | 10.1083/jcb.201106079 | keywords          | 0
    | 10.7554/eLife.000536  | keywords          | 3
		
    | 10.7554/eLife.00013   | subject_area      | 2
    | 10.1083/jcb.201106079 | subject_area      | 2
    | 10.7554/eLife.000536  | subject_area      | 1
		
    | 10.7554/eLife.00013   | authors           | 8
    | 10.1083/jcb.201106079 | authors           | 4
    | 10.7554/eLife.000536  | authors           | 26
		
    | 10.7554/eLife.00013   | refs              | 105
    | 10.1083/jcb.201106079 | refs              | 57
    | 10.7554/eLife.000536  | refs              | 15
		
    | 10.7554/eLife.00013   | components        | 30
    | 10.7554/eLife.000536  | components        | 1