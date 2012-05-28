Feature: parse the article DOI
	In order to use the DOI of this article
	as a script 
	I will read the DOI article-id node
	
	Scenario: second title of NLM3-sample-for-elife.xml
		Given I have the document "NLM3-sample-for-elife.1.xml" 
		When I get the doi 
		Then I see the identifier 10.1083/jcb.201106079

	Scenario: title of NLM3-sample-for-elife.xml
		Given I have the document "NLM3-sample-for-elife.2.xml" 
		When I get the doi 
		Then I see the identifier 10.1083/jcb.201106010