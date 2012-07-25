Feature: parse the article pmid
	In order to use the DOI of this article
	as a script 
	I will read the pmid article-id node
	
	Scenario: second title of NLM3-sample-for-elife.xml
		Given I have the document "NLM3-sample-for-elife.1.xml" 
		When I get the pmid
		Then I see the number 21911481

	Scenario: title of NLM3-sample-for-elife.xml
		Given I have the document "NLM3-sample-for-elife.2.xml" 
		When I get the pmid
		Then I see the number 21911479