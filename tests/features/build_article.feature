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
		
    | 10.1083/jcb.201106079 | article_institution  | Department of Biochemistry, Stanford University Medical School, Stanford, CA 94305

		| 10.1083/jcb.201106079 | article_type   | research-article
		
    | 10.1083/jcb.201106079 | pub_date_date  | September 19, 2011
		| 10.7554/eLife.000536  | pub_date_date  | June 26, 2012
		
		# Tests expanded for many 10.7554/eLife.00013 data points
		
    | 10.7554/eLife.00013   | about                    | http://dx.doi.org/10.7554/eLife.00013
		| 10.7554/eLife.00013   | abstract                 | Bacterially-produced small molecules exert profound influences on animal health, morphogenesis, and evolution through poorly understood mechanisms. In one of the closest living relatives of animals, the choanoflagellate Salpingoeca rosetta, we find that rosette colony development is induced by the prey bacterium Algoriphagus machipongonensis and its close relatives in the Bacteroidetes phylum. Here we show that a rosette inducing factor (RIF-1) produced by A. machipongonensis belongs to the small class of sulfonolipids, obscure relatives of the better known sphingolipids that play important roles in signal transmission in plants, animals, and fungi. RIF-1 has extraordinary potency (femtomolar, or 10−15 M) and S. rosetta can respond to it over a broad dynamic range—nine orders of magnitude. This study provides a prototypical example of bacterial sulfonolipids triggering eukaryotic morphogenesis and suggests molecular mechanisms through which bacteria may have contributed to the evolution of animals.
		
		| 10.7554/eLife.00013   | accepted_date_date       | July 18, 2012
		| 10.7554/eLife.00013   | accepted_date_day        | 18
		| 10.7554/eLife.00013   | accepted_date_month      | 7
		| 10.7554/eLife.00013   | accepted_date_timestamp  | 1342569600
		| 10.7554/eLife.00013   | accepted_date_year       | 2012
		| 10.7554/eLife.00013   | ack                      | AcknowledgementsWe thank Michael Fischbach, Richard Losick, and Russell Vance for critical reading of the manuscript. NK is a Fellow in the Integrated Microbial Biodiversity Program of the Canadian Institute for Advanced Research.
    | 10.7554/eLife.00013   | article_country          | None
    | 10.7554/eLife.00013   | article_institution      | None
    | 10.7554/eLife.00013   | article_title            | A bacterial sulfonolipid triggers multicellular development in the closest living relatives of animals
		| 10.7554/eLife.00013   | article_type             | research-article
		| 10.7554/eLife.00013   | author_notes             | †These authors contributed equally to this work.
    | 10.7554/eLife.00013   | authors[0]['position']   | 1
    | 10.7554/eLife.00013   | authors[1]['about']      | author_2_10.7554/eLife.00013
    | 10.7554/eLife.00013   | authors[2]['article_doi']   | 10.7554/eLife.00013
    | 10.7554/eLife.00013   | authors[3]['city']          | Boston
    | 10.7554/eLife.00013   | authors[4]['country']       | United States
    | 10.7554/eLife.00013   | authors[5]['department']    | Department of Molecular and Cell Biology
    | 10.7554/eLife.00013   | authors[6]['given_names']   | Jon
    | 10.7554/eLife.00013   | authors[7]['institution']   | University of California, Berkeley
    | 10.7554/eLife.00013   | authors[0]['equal_contrib'] | True
		| 10.7554/eLife.00013   | award_group_award_id        | F32 GM086054
		| 10.7554/eLife.00013   | award_group_funding_source  | Gordon and Betty Moore Foundation Marine Microbiology Initiative
		| 10.7554/eLife.00013   | award_group_principle_award_recipient  | Nicole King
		| 10.7554/eLife.00013   | components[0]['about']      | http://dx.doi.org/10.7554/eLife.00013.001
		| 10.7554/eLife.00013   | components[1]['article_doi']| 10.7554/eLife.00013
		| 10.7554/eLife.00013   | components[2]['content']    | Figure 1. Rosette colony development in S. rosetta is regulated by A. machipongonensis . ( A ) The original culture of S. rosetta , ATCC 50818, contains diverse co-isolated environmental bacteria and forms rosette colonies (arrowheads) rarely. ( B ) Treatment of ATCC50818 with a cocktail of antibiotics reduced the bacterial diversity and yielded an S. rosetta culture line, RCA, in which rosette colonies never formed. (Representative single cells indicated by arrows.) ( C ) Addition of A. machipongonensis to RCA cultures was sufficient to induce rosette development. Scale bar, 2 μm. DOI:  http://dx.doi.org/elife/10.7554/eLife.00013.003
		| 10.7554/eLife.00013   | components[3]['doi']        | 10.7554/eLife.00013.004
		| 10.7554/eLife.00013   | components[4]['doi_url']    | http://dx.doi.org/10.7554/eLife.00013.005
		| 10.7554/eLife.00013   | components[5]['position']   | 6
		| 10.7554/eLife.00013   | components[6]['type']       | table-wrap
		| 10.7554/eLife.00013   | conflict                    | The remaining authors have no competing interests to declare.
		| 10.7554/eLife.00013   | copyright_holder            | Alegado et al
		| 10.7554/eLife.00013   | copyright_statement         | Copyright © 2012, Alegado et al
		| 10.7554/eLife.00013   | copyright_year              | 2012
		| 10.7554/eLife.00013   | correspondence              | *For correspondence: jon_clardy@hms.harvard.edu (JC); nking@berkeley.edu (NK)
    | 10.7554/eLife.00013   | doi                         | 10.7554/eLife.00013
    | 10.7554/eLife.00013   | doi_url                     | http://dx.doi.org/10.7554/eLife.00013
		| 10.7554/eLife.00013   | funding_statement           | The funders had no role in study design, data collection and interpretation, or the decision to submit the work for publication.
		| 10.7554/eLife.00013   | journal_id                  | elife
		| 10.7554/eLife.00013   | journal_issn_epub           | 2050-084X
		| 10.7554/eLife.00013   | journal_issn_ppub           | None
		| 10.7554/eLife.00013   | journal_title               | eLife
		| 10.7554/eLife.00013   | keywords[2]                 | bacterial sulfonolipid
		| 10.7554/eLife.00013   | license                     | This article is distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use and redistribution provided that the original author and source are credited.
		| 10.7554/eLife.00013   | license_type                | open-access
		| 10.7554/eLife.00013   | license_url                 | http://creativecommons.org/licenses/by/3.0/
    | 10.7554/eLife.00013   | pmid                        | None
    | 10.7554/eLife.00013   | pub_date_date               | October 15, 2012
		| 10.7554/eLife.00013   | pub_date_day                | 15
		| 10.7554/eLife.00013   | pub_date_month              | 10
		| 10.7554/eLife.00013   | pub_date_timestamp          | 1350259200
		| 10.7554/eLife.00013   | pub_date_year               | 2012
		| 10.7554/eLife.00013   | publisher                   | eLife Sciences Publications, Ltd
		| 10.7554/eLife.00013   | received_date_date          | May 22, 2012
		| 10.7554/eLife.00013   | received_date_day           | 22
		| 10.7554/eLife.00013   | received_date_month         | 5
		| 10.7554/eLife.00013   | received_date_timestamp     | 1337644800
		| 10.7554/eLife.00013   | received_date_year          | 2012
    | 10.7554/eLife.00013   | refs[0]['year']             | 1992
    | 10.7554/eLife.00013   | refs[0]['publication_type'] | book
    | 10.7554/eLife.00013   | refs[0]['publisher_loc']    | New York
    | 10.7554/eLife.00013   | refs[0]['publisher_name']   | Scientific American Press
    | 10.7554/eLife.00013   | refs[1]['volume']           | 57
    | 10.7554/eLife.00013   | refs[2]['source']           | Int J Syst Evol Microbiol
    | 10.7554/eLife.00013   | refs[3]['ref']              | An D Na C Bielawski J Hannun YA Kasper DL. 2011. Membrane sphingolipids as essential molecular signals for Bacteroides survival in the intestine. Proc Natl Acad Sci U S A 108 Suppl. 1: 4666 – 4671.
    | 10.7554/eLife.00013   | refs[4]['publication_type'] | journal
    | 10.7554/eLife.00013   | refs[5]['position']         | 6
    | 10.7554/eLife.00013   | refs[6]['fpage']            | 2051
    | 10.7554/eLife.00013   | refs[7]['lpage']            | 997
    | 10.7554/eLife.00013   | refs[8]['authors'][0]       | Bernardet J
    | 10.7554/eLife.00013   | refs[9]['article_title']    | The complete genome sequence of Escherichia coli K-12
    | 10.7554/eLife.00013   | refs[10]['article_doi']     | 10.7554/eLife.00013
    | 10.7554/eLife.00013   | refs[11]['about']           | ref_12_10.7554/eLife.00013
		| 10.7554/eLife.00013   | research_organism           | Other
		| 10.7554/eLife.00013   | subject_area[0]             | Research article
		| 10.7554/eLife.00013   | subject_area[1]             | Cell biology
		

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
		
    | 10.7554/eLife.00013   | research_organism | 1
    | 10.7554/eLife.00013   | journal_issn_ppub | 0
    | 10.7554/eLife.00013   | article_country   | 0
    | 10.7554/eLife.00013   | article_institution   | 0
		