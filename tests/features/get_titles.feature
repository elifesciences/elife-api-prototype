Feature: parse the title
	In order to parse an xml document 
	as a script 
	I will read the title node
	
	Scenario: title of NLM3-sample-for-elife.xml
		Given I have the document "NLM3-sample-for-elife.2.xml" 
		When I get the title 
		Then I see the string "Arf6 regulates AP-1B&#x02013;dependent sorting in polarized epithelial cells"	

	Scenario: second title of NLM3-sample-for-elife.xml
		Given I have the document "NLM3-sample-for-elife.1.xml" 
		When I get the title 
		Then I see the string "CENP-C recruits M18BP1 to centromeres to promote CENP-A chromatin assembly"