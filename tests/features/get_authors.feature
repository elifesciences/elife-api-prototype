Feature: get authors from the document
	In order to put my author names in my api
	as a script 
	I will parse the authors from the xml file
	
	Scenario: second title of NLM3-sample-for-elife.xml
		Given I have the document "NLM3-sample-for-elife.1.xml" 
		When I count the number of authors
		Then I see the number 4

	Scenario: title of NLM3-sample-for-elife.xml
		Given I have the document "NLM3-sample-for-elife.2.xml" 
		When I count the number of authors
		Then I see the number 3