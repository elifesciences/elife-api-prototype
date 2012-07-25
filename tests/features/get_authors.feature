Feature: get authors from the document
	In order to put my author names in my api
	as a script 
	I will parse the authors from the xml file
	
	Scenario: number of authors of NLM3-sample-for-elife.xml
		Given I have the document "NLM3-sample-for-elife.1.xml" 
		When I count the number of authors
		Then I count the total authors as 4

	Scenario: number of authors of NLM3-sample-for-elife.xml
		Given I have the document "NLM3-sample-for-elife.2.xml" 
		When I count the number of authors
		Then I count the total authors as 3