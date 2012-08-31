import settings

namespaces = [
  {'namespace': 'article'},
  {'namespace': 'person'},
  {'namespace': 'ref'},
  {'namespace': 'alm'},
  {'namespace': 'alm_source'},
]

tags = [
  {'tag': 'article/doi',		'desc': ''},
  {'tag': 'article/doi_url',		'desc': ''},
  {'tag': 'article/pmid',		'desc': ''},
  {'tag': 'article/journal_id',		'desc': ''},
  {'tag': 'article/journal_title',		'desc': ''},
  {'tag': 'article/journal_issn_ppub',		'desc': ''},
  {'tag': 'article/journal_issn_epub',		'desc': ''},
  {'tag': 'article/publisher',		'desc': ''},
  {'tag': 'article/article_title',		'desc': ''},
  {'tag': 'article/abstract',		'desc': ''},
  {'tag': 'article/article_type',		'desc': ''},
  {'tag': 'article/article_institution',		'desc': ''},
  {'tag': 'article/article_country',		'desc': ''},
  {'tag': 'article/subject_area',		'desc': ''},
  {'tag': 'article/research_organism',		'desc': ''},
  {'tag': 'article/authors',		'desc': ''},
  {'tag': 'article/authors_id',		'desc': ''},
  {'tag': 'article/authors_surname',		'desc': ''},
  {'tag': 'article/authors_given_names',		'desc': ''},
  {'tag': 'article/authors_department',		'desc': ''},
  {'tag': 'article/authors_institution',		'desc': ''},
  {'tag': 'article/authors_city',		'desc': ''},
  {'tag': 'article/authors_country',		'desc': ''},
  {'tag': 'article/authors_corresponding',		'desc': ''},
  {'tag': 'article/authors_corresponding_surname',		'desc': ''},
  {'tag': 'article/authors_corresponding_given_names',		'desc': ''},
  {'tag': 'article/authors_corresponding_department',		'desc': ''},
  {'tag': 'article/authors_corresponding_institution',		'desc': ''},
  {'tag': 'article/authors_corresponding_city',		'desc': ''},
  {'tag': 'article/authors_corresponding_country',		'desc': ''},
  {'tag': 'article/correspondence',		'desc': ''},
  {'tag': 'article/author_notes',		'desc': ''},
  {'tag': 'article/keywords',		'desc': ''},
  {'tag': 'article/pub_date_date',		'desc': ''},
  {'tag': 'article/pub_date_day',		'desc': ''},
  {'tag': 'article/pub_date_month',		'desc': ''},
  {'tag': 'article/pub_date_year',		'desc': ''},
  {'tag': 'article/pub_date_timestamp',		'desc': ''},
  {'tag': 'article/received_date_date',		'desc': ''},
  {'tag': 'article/received_date_day',		'desc': ''},
  {'tag': 'article/received_date_month',		'desc': ''},
  {'tag': 'article/received_date_year',		'desc': ''},
  {'tag': 'article/received_date_timestamp',		'desc': ''},
  {'tag': 'article/accepted_date_date',		'desc': ''},
  {'tag': 'article/accepted_date_day',		'desc': ''},
  {'tag': 'article/accepted_date_month',		'desc': ''},
  {'tag': 'article/accepted_date_year',		'desc': ''},
  {'tag': 'article/accepted_date_timestamp',		'desc': ''},
  {'tag': 'article/award_group_funding_source',		'desc': ''},
  {'tag': 'article/award_group_award_id',		'desc': ''},
  {'tag': 'article/award_group_principle_award_recipient',		'desc': ''},
  {'tag': 'article/funding_statement',		'desc': ''},
  {'tag': 'article/copyright_statement',		'desc': ''},
  {'tag': 'article/copyright_year',		'desc': ''},
  {'tag': 'article/copyright_holder',		'desc': ''},
  {'tag': 'article/license',		'desc': ''},
  {'tag': 'article/license_type',		'desc': ''},
  {'tag': 'article/license_url',		'desc': ''},
  {'tag': 'article/ack',		'desc': ''},
  {'tag': 'article/conflict',		'desc': ''},
  {'tag': 'article/refs',		'desc': ''},
  {'tag': 'article/refs_publication_type',		'desc': ''},
  {'tag': 'article/refs_article_title',		'desc': ''},
  {'tag': 'article/refs_authors',		'desc': ''},
  {'tag': 'article/refs_year',		'desc': ''},
  {'tag': 'article/refs_source',		'desc': ''},
  {'tag': 'article/refs_volume',		'desc': ''},
  {'tag': 'article/refs_fpage',		'desc': ''},
  {'tag': 'article/refs_lpage',		'desc': ''},
  {'tag': 'article/refs_doi',		'desc': ''},
  {'tag': 'article/refs_pmid',		'desc': ''},
  {'tag': 'article/refs_collab',		'desc': ''},
  {'tag': 'article/refs_publisher_loc',		'desc': ''},
  {'tag': 'article/refs_publisher_name',		'desc': ''},
  {'tag': 'article/citation',		'desc': ''},
  {'tag': 'article/xml',		'desc': ''},
  
  {'tag': 'person/surname',		'desc': ''},
  
  {'tag': 'ref/ref',		'desc': ''},
  {'tag': 'ref/article_title',		'desc': ''},
  {'tag': 'ref/publication_type',		'desc': ''},
  {'tag': 'ref/doi',		'desc': ''},
  {'tag': 'ref/pmid',		'desc': ''},
  {'tag': 'ref/authors',		'desc': ''},
  {'tag': 'ref/year',		'desc': ''},
  {'tag': 'ref/source',		'desc': ''},
  {'tag': 'ref/volume',		'desc': ''},
  {'tag': 'ref/fpage',		'desc': ''},
  {'tag': 'ref/lpage',		'desc': ''},
  {'tag': 'ref/collab',		'desc': ''},
  {'tag': 'ref/publisher_loc',		'desc': ''},
  {'tag': 'ref/publisher_name',		'desc': ''},

  {'tag': 'alm_source/source',		'desc': ''},
  {'tag': 'alm_source/url',		'desc': ''},
  {'tag': 'alm_source/name',		'desc': ''},
  {'tag': 'alm_source/trusted',		'desc': ''},
	
  {'tag': 'alm/doi',		'desc': ''},
  {'tag': 'alm/source',		'desc': ''},
  {'tag': 'alm/type',		'desc': ''},
  {'tag': 'alm/value',		'desc': ''},
  {'tag': 'alm/timespan',		'desc': ''},
  {'tag': 'alm/date_date',		'desc': ''},
  {'tag': 'alm/date_day',		'desc': ''},
  {'tag': 'alm/date_month',		'desc': ''},
  {'tag': 'alm/date_year',		'desc': ''},
  {'tag': 'alm/date_timestamp',		'desc': ''},
  {'tag': 'alm/complete',		'desc': ''},
  {'tag': 'alm/temp_key',		'desc': ''},
]

objects = [
    {'obj': 'df97444e-9579-49f1-8302-2dce51c0bd95', 'key': 'article/doi', 'article/doi': '10.7554/eLife.000536', 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'article/doi = "10.7554/eLife.000536"',
            {
             settings.namespace + '/' + 'article/doi': {'value': '10.7554/eLife.000536'},
             settings.namespace + '/' + 'article/doi_url': {'value': 'http://dx.doi.org/10.7554/eLife.000536'},
             #settings.namespace + '/' + 'article/pmid': {'value': ''},
             settings.namespace + '/' + 'article/journal_id': {'value': 'eLife'},
             settings.namespace + '/' + 'article/journal_title': {'value': 'eLife'},
             #settings.namespace + '/' + 'article/journal_issn_ppub': {'value': ''},
             settings.namespace + '/' + 'article/journal_issn_epub': {'value': '2050-084X'},
             settings.namespace + '/' + 'article/publisher': {'value': 'eLife Sciences Publications, Ltd'},
             settings.namespace + '/' + 'article/article_title': {'value': 'Prophylactic Platelets in Dengue: Survey Responses Highlight Lack of an Evidence Base'},
             settings.namespace + '/' + 'article/abstract': {'value': '<title>Textbook Summary</title><p>A low platelet count is a common feature of dengue infection. It is thought that the platelet count correlates with the severity of the infection and may contribute to the risk of developing haemorrhage, a well-recognised complication of dengue. As a result of this platelet transfusions are used in some settings to reduce the risk of haemorrhage. There is currently no evidence to support this practice, and platelet transfusions are costly and sometimes harmful. We conducted a survey assessing the use of platelets in dengue. Respondents were all physicians involved with the treatment of patients with dengue. Respondents were asked that their answers reflected what they would do if they were the treating physician. We received 306 responses from 20 different countries. The striking feature of the survey responses was the heterogeneity of approaches to the use of platelets in dengue. These findings highlight the variation in clinical practice and lack of an evidence base in this area and underscore the importance of conducting prospective clinical trials to address this key question in dengue clinical management.</p>'},
             settings.namespace + '/' + 'article/article_type': {'value': 'Research'},
             settings.namespace + '/' + 'article/article_institution': {'value': 'Pediatric Dengue Vaccine Initiative'},
             settings.namespace + '/' + 'article/article_country': {'value': 'United States of America'},
             settings.namespace + '/' + 'article/subject_area': {'value': 'Microbiology and infectious disease'},
             settings.namespace + '/' + 'article/research_organism': {'value': 'None'},
             settings.namespace + '/' + 'article/authors': {'value': ['James Whitehorn','Rosmari Rodriguez Roche','Maria G. Guzman','Eric Martinez','Wilmar Villamil Gomez','Leonard Nainggolan','Ida Safitri Laksono','Ajay Mishra','Lucy Lum','Abul Faiz','Amadou Sall','Joshua Dawurung','Alvaro Borges','Yee-Sin Leo','Lucille Blumberg','Daniel G. Bausch','Axel Kroeger','Olaf Horstick','Guy Thwaites','Heiman Wertheim','Mattias Larsson','Tran Tinh Hien','Rosanna Peeling','Bridget Wills','Cameron Simmons','Jeremy Farrar']},
             settings.namespace + '/' + 'article/authors_id': {'value': ['','','','','','','','','','','','','','','','','','','','','','','','','','']},
             settings.namespace + '/' + 'article/authors_surname': {'value': ['Whitehorn','Roche','Guzman','Martinez','Villamil Gomez','Nainggolan','Laksono','Mishra','Lum','Faiz','Sall','Dawurung','Borges','Leo','Blumberg','Bausch','Kroeger','Horstick','Thwaites','Wertheim','Larsson','Hien','Peeling','Wills','Simmons','Farrar']},
             settings.namespace + '/' + 'article/authors_given_names': {'value': ['James','Rosmari Rodriguez','Maria G.','Eric','Wilmar','Leonard','Ida Safitri','Ajay','Lucy','Abul','Amadou','Joshua','Alvaro','Yee-Sin','Lucille','Daniel G.','Axel','Olaf','Guy','Heiman','Mattias','Tran Tinh','Rosanna','Bridget','Cameron','Jeremy']},
             settings.namespace + '/' + 'article/authors_department': {'value': ['Department of Clinical Research; Oxford University Clinical Research Unit', '', '', '', '', '', 'Paediatric Department', '', 'Department of Paediatrics', '', '', '', 'Copenhagen HIV Programme; ', 'Department of Infectious Diseases', '', '', 'Special Programme for Research and Training in Tropical Diseases', '', 'Department of Infectious Disease/Centre for Clinical Infection and Diagnostics Research', 'Oxford University Clinical Research Unit', 'Oxford University Clinical Research Unit', 'Oxford University Clinical Research Unit', 'Department of Clinical Research', 'Oxford University Clinical Research Unit', 'Oxford University Clinical Research Unit', 'Oxford University Clinical Research Unit']},
             settings.namespace + '/' + 'article/authors_institution': {'value': ['London School of Hygiene and Tropical Medicine; Hospital for Tropical Diseases', 'Instituto de Medicina Tropical Pedro Kouri', 'Instituto de Medicina Tropical Pedro Kouri', 'Instituto de Medicina Tropical Pedro Kouri', 'Hospital Universitario de Sincelejo', 'University of Indonesia', 'Gadjah Mada University', 'Sunderlal Memorial Hospital', 'University of Malaya', 'Sir Sallimullah Medical College', 'Institute Pasteur', 'University of Maiduguri Teaching Hospital', 'University of Copenhagen; University Hospital, Federal University of Minas Gerais', 'Tan Tock Seng Hospital', 'National Institute for Communicable Diseases', 'Tulane School of Public Health and Tropical Medicine', 'World Health Organization', 'Institute of Public Health, University of Heidelberg', 'King\'s College London', 'Hospital for Tropical Diseases', 'Hospital for Tropical Diseases', 'Hospital for Tropical Diseases', 'London School of Hygiene and Tropical Medicine', 'Hospital for Tropical Diseases', 'Hospital for Tropical Diseases', 'Hospital for Tropical Diseases']},
             settings.namespace + '/' + 'article/authors_city': {'value': ['London; Ho Chi Minh City', 'Havana', 'Havana', 'Havana', 'Sincelejo', 'Jakarta', 'Yogyakarta', 'Delhi', 'Kuala Lumpur', 'Dhaka', 'Dakar', 'Borno State', 'Copenhagen; Belo Horizonte', 'Singapore', 'Johannesburg', 'New Orleans, Louisiana', 'Geneva', 'Heidelberg', 'London', 'Ho Chi Minh City', 'Ho Chi Minh City', 'Ho Chi Minh City', 'London', 'Ho Chi Minh City', 'Ho Chi Minh City', 'Ho Chi Minh City']},
             settings.namespace + '/' + 'article/authors_country': {'value': ['United Kingdom; Vietnam', 'Cuba', 'Cuba', 'Cuba', 'Colombia', 'Indonesia', 'Indonesia', 'India', 'Malaysia', 'Bangladesh', 'Senegal', 'Nigeria', 'Denmark; Brazil', 'Singapore', 'South Africa', 'United States of America', 'Switzerland', 'Germany', 'United Kingdom', 'Vietnam', 'Vietnam', 'Vietnam', 'United Kingdom', 'Vietnam', 'Vietnam', 'Vietnam']},
             settings.namespace + '/' + 'article/authors_corresponding': {'value': 'James Whitehorn'},
             settings.namespace + '/' + 'article/authors_corresponding_surname': {'value': 'Whitehorn'},
             settings.namespace + '/' + 'article/authors_corresponding_given_names': {'value': 'James'},
             settings.namespace + '/' + 'article/authors_corresponding_department': {'value': 'Department of Clinical Research; Oxford University Clinical Research Unit'},
             settings.namespace + '/' + 'article/authors_corresponding_institution': {'value': 'London School of Hygiene and Tropical Medicine;  Hospital for Tropical Diseases'},
             settings.namespace + '/' + 'article/authors_corresponding_city': {'value': 'London; Ho Chi Minh City'},
             settings.namespace + '/' + 'article/authors_corresponding_country': {'value': 'United Kingdom; Vietnam'},
             settings.namespace + '/' + 'article/correspondence': {'value': '<label>&#x002A;</label>For correspondence: <email>james.whitehorn@lshtm.ac.uk</email> (JW)'},
             settings.namespace + '/' + 'article/author_notes': {'value': """<label>Author Contributions</label>
		<p>Conception and design: JW, BW, JF, TTH</p>
		<p>Acquisition of data: JW, BW, JF, TTH</p>
		<p>Analysis and interpretation of data: JW, BW, JF, TTH</p>
		<p>Drafting or revising the article: JW, BW, JF, TTH</p>
		<p>Contributed unpublished essential data or reagents: JW, BW, JF, TTH</p>
		<p>Drafting or revising the article: JW, BW, JF, TTH</p>
		<p>INSERT TEXT FROM FREEFORM BOX: AUTHOR INITIALS</p>"""},
             settings.namespace + '/' + 'article/keywords': {'value': ['platelets','dengue','thrombocytopenia']},
             settings.namespace + '/' + 'article/pub_date_date': {'value': 'June 26, 2012'},
             settings.namespace + '/' + 'article/pub_date_day': {'value': '26'},
             settings.namespace + '/' + 'article/pub_date_month': {'value': '6'},
             settings.namespace + '/' + 'article/pub_date_year': {'value': '2012'},
             settings.namespace + '/' + 'article/pub_date_timestamp': {'value': '1340668800'},
             settings.namespace + '/' + 'article/received_date_date': {'value': 'March 30, 2012'},
             settings.namespace + '/' + 'article/received_date_day': {'value': '30'},
             settings.namespace + '/' + 'article/received_date_month': {'value': '3'},
             settings.namespace + '/' + 'article/received_date_year': {'value': '2012'},
             settings.namespace + '/' + 'article/received_date_timestamp': {'value': '1333065600'},
             settings.namespace + '/' + 'article/accepted_date_date': {'value': 'May 17, 2012'},
             settings.namespace + '/' + 'article/accepted_date_day': {'value': '17'},
             settings.namespace + '/' + 'article/accepted_date_month': {'value': '5'},
             settings.namespace + '/' + 'article/accepted_date_year': {'value': '2012'},
             settings.namespace + '/' + 'article/accepted_date_timestamp': {'value': '1337212800'},
             settings.namespace + '/' + 'article/award_group_funding_source': {'value': 'National Institutes of Health'},
             settings.namespace + '/' + 'article/award_group_award_id': {'value': 'GM18458'},
             settings.namespace + '/' + 'article/award_group_principle_award_recipient': {'value': 'Author name(s)'},
             settings.namespace + '/' + 'article/funding_statement': {'value': 'The funding sources were not involved in study design; collection, analysis, and interpretation of data; writing the article; and/or the decision to submit to the journal'},
             settings.namespace + '/' + 'article/copyright_statement': {'value': 'Copyright &#x00A9; 2012, Whitehorn et al.'},
             settings.namespace + '/' + 'article/copyright_year': {'value': '2012'},
             settings.namespace + '/' + 'article/copyright_holder': {'value': 'Whitehorn et al.'},
             settings.namespace + '/' + 'article/license': {'value': ' This work is licensed under a Creative Commons Attribution 3.0 Unported License. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.'},
             settings.namespace + '/' + 'article/license_type': {'value': 'open-access'},
             settings.namespace + '/' + 'article/license_url': {'value': 'http://creativecommons.org/licenses/by/3.0/'},
             settings.namespace + '/' + 'article/ack': {'value': '<p>The authors would like to thank Dr Osvaldo Castro from IPK in Cuba for his assistance in distributing the questionnaires.</p>'},
             settings.namespace + '/' + 'article/conflict': {'value': """<label>Competing interests</label>
	<p>The authors have declared that no competing interests exist.</p>"""},
             settings.namespace + '/' + 'article/refs': {'value': ['Guzman MG, Halstead SB, Artsob H, Buchy P, Farrar J, et al. (2010) Dengue: a continuing global threat. Nat Rev Microbiol 8: S7&#x2013;S16.', 'Lee VJ, Lye DC, Sun Y, Fernandez G, Ong A, et al. (2008) Predictive value of simple clinical and laboratory variables for dengue hemorrhagic fever in adults. J Clin Virol 42: 34&#x2013;39', 'La Russa VF, Innis BL (1995) Mechanisms of dengue virus-induced bone marrow suppression. Baillieres Clin Haematol 8: 249&#x2013;270', 'Lei HY, Yeh TM, Liu HS, Lin YS, Chen SH, et al. (2001) Immunopathogenesis of dengue virus infection. J Biomed Sci 8: 377&#x2013;388', 'Alonzo MT, Lacuesta TL, Dimaano EM, Kurosu T, Suarez LA, et al. (2012) Platelet apoptosis and apoptotic platelet clearance by macrophages in secondary dengue virus infections. J Infect Dis 205: 1321&#x2013;1329', 'Krishnamurti C, Kalayanarooj S, Cutting MA, Peat RA, Rothwell SW, et al. (2001) Mechanisms of hemorrhage in dengue without circulatory collapse. Am J Trop Med Hyg 65: 840&#x2013;847', 'Noisakran S, Chokephaibulkit K, Songprakhon P, Onlamoon N, Hsiao HM, et al. (2009) A re-evaluation of the mechanisms leading to dengue hemorrhagic fever. Ann N Y Acad Sci 1171: E24&#x2013;35', 'WHO (2009) Dengue: guidelines for diagnosis, treatment, prevention and control - New edition. Geneva: World Health Organisation.', 'WHO (2011) Comprehensive guidelines for the prevention and control of dengue and dengue haemorrhagic fever, revised and expanded edition.. In: Asia ROfS-E, editor. Delhi.', 'India Go (2008) Guidelines for clinical management of dengue fever, dengue haemorrhagic fever and dengue shock syndrome. In: Programme DoNVBDC, editor. Delhi.', 'Verdeal J, Filho RC, Vanzillotta C, Macedo G, Bozza F, et al. (2011) Guidelines for the management of patients with severe forms of dengue. Rev Bras Ter Intensiva 23: 125&#x2013;133', 'Lum LC, Abdel-Latif Mel A, Goh AY, Chan PW, Lam SK (2003) Preventive transfusion in Dengue shock syndrome-is it necessary? J Pediatr 143: 682&#x2013;684', 'Lye DC, Lee VJ, Sun Y, Leo YS (2009) Lack of efficacy of prophylactic platelet transfusion for severe thrombocytopenia in adults with acute uncomplicated dengue infection. Clin Infect Dis 48: 1262&#x2013;1265', 'Kurukularatne C, Dimatatac F, Teo DL, Lye DC, Leo YS (2011) When less is more: can we abandon prophylactic platelet transfusion in Dengue fever? Ann Acad Med Singapore 40: 539&#x2013;537', 'Sharma A, Charles K, Chadee D, Teelucksingh S (2012) Dengue hemorrhagic Fever in trinidad and tobago: a case for a conservative approach to platelet transfusion. Am J Trop Med Hyg 86: 531&#x2013;535']},
             settings.namespace + '/' + 'article/refs_publication_type': {'value': ['journal', 'journal', 'journal', 'journal', 'journal', 'journal', 'journal', 'book', 'book', 'other', 'journal', 'journal', 'journal', 'journal', 'journal']},
             settings.namespace + '/' + 'article/refs_article_title': {'value': ['Dengue: a continuing global threat', 'Predictive value of simple clinical and laboratory variables for dengue hemorrhagic fever in adults', 'Mechanisms of dengue virus-induced bone marrow suppression', 'Immunopathogenesis of dengue virus infection', 'Platelet apoptosis and apoptotic platelet clearance by macrophages in secondary dengue virus infections', 'Mechanisms of hemorrhage in dengue without circulatory collapse', 'A re-evaluation of the mechanisms leading to dengue hemorrhagic fever', 'Dengue: guidelines for diagnosis, treatment, prevention and control - New edition', 'Comprehensive guidelines for the prevention and control of dengue and dengue haemorrhagic fever, revised and expanded edition', 'Guidelines for clinical management of dengue fever, dengue haemorrhagic fever and dengue shock syndrome', 'Guidelines for the management of patients with severe forms of dengue', 'Preventive transfusion in Dengue shock syndrome-is it necessary?', 'Lack of efficacy of prophylactic platelet transfusion for severe thrombocytopenia in adults with acute uncomplicated dengue infection', 'When less is more: can we abandon prophylactic platelet transfusion in Dengue fever?', 'Dengue hemorrhagic Fever in trinidad and tobago: a case for a conservative approach to platelet transfusion']},
             settings.namespace + '/' + 'article/refs_authors': {'value': ['Guzman MG, Halstead SB, Artsob H, Buchy P, Farrar J, et al.', 'Lee VJ, Lye DC, Sun Y, Fernandez G, Ong A, et al.', 'La Russa VF, Innis BL', 'Lei HY, Yeh TM, Liu HS, Lin YS, Chen SH, et al.', 'Alonzo MT, Lacuesta TL, Dimaano EM, Kurosu T, Suarez LA, et al.', 'Krishnamurti C, Kalayanarooj S, Cutting MA, Peat RA, Rothwell SW, et al.', 'Noisakran S, Chokephaibulkit K, Songprakhon P, Onlamoon N, Hsiao HM, et al.', '', '', 'India Go', 'Verdeal J, Filho RC, Vanzillotta C, Macedo G, Bozza F, et al.', 'Lum LC, Abdel-Latif Mel A, Goh AY, Chan PW, Lam SK', 'Lye DC, Lee VJ, Sun Y, Leo YS', 'Kurukularatne C, Dimatatac F, Teo DL, Lye DC, Leo YS', 'Sharma A, Charles K, Chadee D, Teelucksingh S']},
             settings.namespace + '/' + 'article/refs_year': {'value': ['2010', '2008', '1995', '2001', '2012', '2001', '2009', '2009', '2011', '2008', '2011', '2003', '2009', '2011', '2012']},
             settings.namespace + '/' + 'article/refs_source': {'value': ['Nat Rev Microbiol', 'J Clin Virol', 'Baillieres Clin Haematol', 'J Biomed Sci', 'J Infect Dis', 'Am J Trop Med Hyg', 'Ann N Y Acad Sci', '', '', '', 'Rev Bras Ter Intensiva', 'J Pediatr', 'Clin Infect Dis', 'Ann Acad Med Singapore', 'Am J Trop Med Hyg']},
             settings.namespace + '/' + 'article/refs_volume': {'value': ['8', '42', '8', '8', '205', '65', '1171', '', '', '', '23', '143', '48', '40', '86']},
             settings.namespace + '/' + 'article/refs_fpage': {'value': ['S7', '34', '249', '377', '1321', '840', 'E24', '', '', '', '125', '682', '1262', '539', '531']},
             settings.namespace + '/' + 'article/refs_lpage': {'value': ['S16', '39', '270', '388', '1329', '847', '35', '', '', '', '133', '684', '1265', '537', '535']},
             settings.namespace + '/' + 'article/refs_doi': {'value': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']},
             settings.namespace + '/' + 'article/refs_pmid': {'value': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']},
             settings.namespace + '/' + 'article/refs_collab': {'value': ['', '', '', '', '', '', '', 'WHO', 'WHO', '', '', '', '', '', '']},
             settings.namespace + '/' + 'article/refs_publisher_loc': {'value': ['', '', '', '', '', '', '', 'Geneva', '', '', '', '', '', '', '']},
             settings.namespace + '/' + 'article/refs_publisher_name': {'value': ['', '', '', '', '', '', '', 'World Health Organisation', '', '', '', '', '', '', '']},
             
             #settings.namespace + '/' + 'article/citation': {'value': ''},
             settings.namespace +  '/' + 'article/xml': {'value': """<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE article PUBLIC "-//NLM//DTD Journal Publishing DTD v3.0 20080202//EN" "journalpublishing3.dtd"><article xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:mml="http://www.w3.org/1998/Math/MathML" article-type="research-article"><front><journal-meta><journal-id journal-id-type="nlm-ta">eLife</journal-id><journal-id journal-id-type="hwp">eLife</journal-id><journal-id journal-id-type="publisher-id">eLife</journal-id><journal-title-group><journal-title>eLife</journal-title></journal-title-group><issn pub-type="epub">2050-084X</issn><publisher><publisher-name>eLife Sciences Publications, Ltd</publisher-name></publisher></journal-meta><article-meta>
<article-id pub-id-type="doi">10.7554/eLife.000536</article-id>
<article-categories>
<subj-group subj-group-type="heading">
<subject>Research</subject>
</subj-group>
</article-categories>
<title-group><article-title>Prophylactic Platelets in Dengue: Survey Responses Highlight Lack of an Evidence Base</article-title></title-group><contrib-group><contrib contrib-type="author" corresp="yes"><name><surname>Whitehorn</surname><given-names>James</given-names></name><xref ref-type="aff" rid="aff1">1</xref><xref ref-type="aff" rid="aff2">2</xref><xref ref-type="corresp" rid="cor1">&#x002A;</xref></contrib><contrib contrib-type="author"><name><surname>Roche</surname><given-names>Rosmari Rodriguez</given-names></name><xref ref-type="aff" rid="aff3">3</xref></contrib><contrib contrib-type="author"><name><surname>Guzman</surname><given-names>Maria G.</given-names></name><xref ref-type="aff" rid="aff3">3</xref></contrib><contrib contrib-type="author"><name><surname>Martinez</surname><given-names>Eric</given-names></name><xref ref-type="aff" rid="aff3">3</xref></contrib><contrib contrib-type="author"><name><surname>Villamil Gomez</surname><given-names>Wilmar</given-names></name><xref ref-type="aff" rid="aff4">4</xref></contrib><contrib contrib-type="author"><name><surname>Nainggolan</surname><given-names>Leonard</given-names></name><xref ref-type="aff" rid="aff5">5</xref></contrib><contrib contrib-type="author"><name><surname>Laksono</surname><given-names>Ida Safitri</given-names></name><xref ref-type="aff" rid="aff6">6</xref></contrib><contrib contrib-type="author"><name><surname>Mishra</surname><given-names>Ajay</given-names></name><xref ref-type="aff" rid="aff7">7</xref></contrib><contrib contrib-type="author"><name><surname>Lum</surname><given-names>Lucy</given-names></name><xref ref-type="aff" rid="aff8">8</xref></contrib><contrib contrib-type="author"><name><surname>Faiz</surname><given-names>Abul</given-names></name><xref ref-type="aff" rid="aff9">9</xref></contrib><contrib contrib-type="author"><name><surname>Sall</surname><given-names>Amadou</given-names></name><xref ref-type="aff" rid="aff10">10</xref></contrib><contrib contrib-type="author"><name><surname>Dawurung</surname><given-names>Joshua</given-names></name><xref ref-type="aff" rid="aff11">11</xref></contrib><contrib contrib-type="author"><name><surname>Borges</surname><given-names>Alvaro</given-names></name><xref ref-type="aff" rid="aff12">12</xref><xref ref-type="aff" rid="aff13">13</xref></contrib><contrib contrib-type="author"><name><surname>Leo</surname><given-names>Yee-Sin</given-names></name><xref ref-type="aff" rid="aff14">14</xref></contrib><contrib contrib-type="author"><name><surname>Blumberg</surname><given-names>Lucille</given-names></name><xref ref-type="aff" rid="aff15">15</xref></contrib><contrib contrib-type="author"><name><surname>Bausch</surname><given-names>Daniel G.</given-names></name><xref ref-type="aff" rid="aff16">16</xref></contrib><contrib contrib-type="author"><name><surname>Kroeger</surname><given-names>Axel</given-names></name><xref ref-type="aff" rid="aff17">17</xref></contrib><contrib contrib-type="author"><name><surname>Horstick</surname><given-names>Olaf</given-names></name><xref ref-type="aff" rid="aff18">18</xref></contrib><contrib contrib-type="author"><name><surname>Thwaites</surname><given-names>Guy</given-names></name><xref ref-type="aff" rid="aff19">19</xref></contrib><contrib contrib-type="author"><name><surname>Wertheim</surname><given-names>Heiman</given-names></name><xref ref-type="aff" rid="aff2">2</xref></contrib><contrib contrib-type="author"><name><surname>Larsson</surname><given-names>Mattias</given-names></name><xref ref-type="aff" rid="aff2">2</xref></contrib><contrib contrib-type="author"><name><surname>Hien</surname><given-names>Tran Tinh</given-names></name><xref ref-type="aff" rid="aff2">2</xref></contrib><contrib contrib-type="author"><name><surname>Peeling</surname><given-names>Rosanna</given-names></name><xref ref-type="aff" rid="aff1">1</xref></contrib><contrib contrib-type="author"><name><surname>Wills</surname><given-names>Bridget</given-names></name><xref ref-type="aff" rid="aff2">2</xref></contrib><contrib contrib-type="author"><name><surname>Simmons</surname><given-names>Cameron</given-names></name><xref ref-type="aff" rid="aff2">2</xref></contrib><contrib contrib-type="author"><name><surname>Farrar</surname><given-names>Jeremy</given-names></name><xref ref-type="aff" rid="aff2">2</xref></contrib></contrib-group><aff id="aff1"><label>1</label><addr-line><named-content content-type="department">Department of Clinical Research</named-content></addr-line>, <institution>London School of Hygiene and Tropical Medicine</institution>, <addr-line><named-content content-type="city">London</named-content></addr-line>, <country>United Kingdom</country></aff><aff id="aff2"><label>2</label><institution>Hospital for Tropical Diseases</institution>, <addr-line><named-content content-type="department">Oxford University Clinical Research Unit</named-content></addr-line>, Wellcome Trust Major Overseas Programme, <addr-line><named-content content-type="city">Ho Chi Minh City</named-content></addr-line>, <country>Vietnam</country></aff><aff id="aff3"><label>3</label><institution>Instituto de Medicina Tropical Pedro Kouri</institution>, <addr-line><named-content content-type="city">Havana</named-content></addr-line>, <country>Cuba</country></aff><aff id="aff4"><label>4</label><institution>Hospital Universitario de Sincelejo</institution>, <addr-line><named-content content-type="city">Sincelejo</named-content></addr-line>, <country>Colombia</country></aff><aff id="aff5"><label>5</label>Faculty of Medicine, <institution>University of Indonesia</institution>, <addr-line><named-content content-type="city">Jakarta</named-content></addr-line>, <country>Indonesia</country></aff><aff id="aff6"><label>6</label><addr-line><named-content content-type="department">Paediatric Department</named-content></addr-line>, <institution>Gadjah Mada University</institution>, <addr-line><named-content content-type="city">Yogyakarta</named-content></addr-line>, <country>Indonesia</country></aff><aff id="aff7"><label>7</label><institution>Sunderlal Memorial Hospital</institution>, <addr-line><named-content content-type="city">Delhi</named-content></addr-line>, <country>India</country></aff><aff id="aff8"><label>8</label><addr-line><named-content content-type="department">Department of Paediatrics</named-content></addr-line>, Faculty of Medicine, <institution>University of Malaya</institution>, <addr-line><named-content content-type="city">Kuala Lumpur</named-content></addr-line>, <country>Malaysia</country></aff><aff id="aff9"><label>9</label><institution>Sir Sallimullah Medical College</institution>, <addr-line><named-content content-type="city">Dhaka</named-content></addr-line>, <country>Bangladesh</country></aff><aff id="aff10"><label>10</label><institution>Institute Pasteur</institution>, <addr-line><named-content content-type="city">Dakar</named-content></addr-line>, <country>Senegal</country></aff><aff id="aff11"><label>11</label><institution>University of Maiduguri Teaching Hospital</institution>, Maiduguri, <addr-line><named-content content-type="city">Borno State</named-content></addr-line>, <country>Nigeria</country></aff><aff id="aff12"><label>12</label><addr-line><named-content content-type="department">Copenhagen HIV Programme</named-content></addr-line>, <institution>University of Copenhagen</institution>, Faculty of Health Sciences, <addr-line><named-content content-type="city">Copenhagen</named-content></addr-line>, <country>Denmark</country></aff><aff id="aff13"><label>13</label><institution>University Hospital, Federal University of Minas Gerais</institution>, <addr-line><named-content content-type="city">Belo Horizonte</named-content></addr-line>, <country>Brazil</country></aff><aff id="aff14"><label>14</label><addr-line><named-content content-type="department">Department of Infectious Diseases</named-content></addr-line>, <institution>Tan Tock Seng Hospital</institution>, <addr-line><named-content content-type="city">Singapore</named-content></addr-line>, <country>Singapore</country></aff><aff id="aff15"><label>15</label><institution>National Institute for Communicable Diseases</institution>, <addr-line><named-content content-type="city">Johannesburg</named-content></addr-line>, <country>South Africa</country></aff><aff id="aff16"><label>16</label><institution>Tulane School of Public Health and Tropical Medicine</institution>, <addr-line><named-content content-type="city">New Orleans, Louisiana</named-content></addr-line>, <country>United States of America</country></aff><aff id="aff17"><label>17</label><addr-line><named-content content-type="deparment">Special Programme for Research and Training in Tropical Diseases</named-content></addr-line>, <institution>World Health Organization</institution>, <addr-line><named-content content-type="city">Geneva</named-content></addr-line>, <country>Switzerland</country></aff><aff id="aff18"><label>18</label><institution>Institute of Public Health, University of Heidelberg</institution>, <addr-line><named-content content-type="city">Heidelberg</named-content></addr-line>, <country>Germany</country></aff><aff id="aff19"><label>19</label><addr-line><named-content content-type="department">Department of Infectious Disease/Centre for Clinical Infection and Diagnostics Research</named-content></addr-line>, <institution>King's College London</institution>, <addr-line><named-content content-type="city">London</named-content></addr-line>, <country>United Kingdom</country></aff><contrib-group content-type="section"><contrib contrib-type="editor"><name><surname>Halstead</surname><given-names>Scott B.</given-names></name><role>Editor</role></contrib><aff><institution>Pediatric Dengue Vaccine Initiative</institution>, <country>United States of America</country></aff></contrib-group><author-notes><corresp id="cor1"><label>&#x002A;</label>For correspondence: <email>james.whitehorn@lshtm.ac.uk</email> (JW)</corresp><fn fn-type="con"><label>Author Contributions</label><p>Conception and design: JW, BW, JF, TTH</p><p>Acquisition of data: JW, BW, JF, TTH</p><p>Analysis and interpretation of data: JW, BW, JF, TTH</p><p>Drafting or revising the article: JW, BW, JF, TTH</p><p>Contributed unpublished essential data or reagents: JW, BW, JF, TTH</p><p>Drafting or revising the article: JW, BW, JF, TTH</p><p>INSERT TEXT FROM FREEFORM BOX: AUTHOR INITIALS</p></fn></author-notes><pub-date pub-type="epub"><day>26</day><month>6</month><year>2012</year></pub-date><volume>6</volume><elocation-id>536</elocation-id><history><date date-type="received"><day>30</day><month>3</month><year>2012</year></date><date date-type="accepted"><day>17</day><month>5</month><year>2012</year></date></history><permissions><copyright-statement>Copyright &#x00A9; 2012, Whitehorn et al.</copyright-statement><copyright-year>2012</copyright-year><copyright-holder>Whitehorn et al.</copyright-holder><license license-type="open-access" xlink:href="http://creativecommons.org/licenses/by/3.0/"><license-p> This work is licensed under a Creative Commons Attribution 3.0 Unported License. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.</license-p></license></permissions><abstract><p>Dengue is the most important arboviral infection of humans. Thrombocytopenia is frequently observed in the course of infection and haemorrhage may occur in severe disease. The degree of thrombocytopenia correlates with the severity of infection, and may contribute to the risk of haemorrhage. As a result of this prophylactic platelet transfusions are sometimes advocated for the prevention of haemorrhage. There is currently no evidence to support this practice, and platelet transfusions are costly and sometimes harmful. We conducted a global survey to assess the different approaches to the use of platelets in dengue. Respondents were all physicians involved with the treatment of patients with dengue. Respondents were asked that their answers reflected what they would do if they were the treating physician. We received responses from 306 physicians from 20 different countries. The heterogeneity of the responses highlights the variation in clinical practice and lack of an evidence base in this area and underscores the importance of prospective clinical trials to address this key question in the clinical management of patients with dengue.</p></abstract><abstract abstract-type="executive-summary"><title>Textbook Summary</title><p>A low platelet count is a common feature of dengue infection. It is thought that the platelet count correlates with the severity of the infection and may contribute to the risk of developing haemorrhage, a well-recognised complication of dengue. As a result of this platelet transfusions are used in some settings to reduce the risk of haemorrhage. There is currently no evidence to support this practice, and platelet transfusions are costly and sometimes harmful. We conducted a survey assessing the use of platelets in dengue. Respondents were all physicians involved with the treatment of patients with dengue. Respondents were asked that their answers reflected what they would do if they were the treating physician. We received 306 responses from 20 different countries. The striking feature of the survey responses was the heterogeneity of approaches to the use of platelets in dengue. These findings highlight the variation in clinical practice and lack of an evidence base in this area and underscore the importance of conducting prospective clinical trials to address this key question in dengue clinical management.</p></abstract><kwd-group kwd-group-type="Research-organism"><kwd>None</kwd></kwd-group><kwd-group kwd-group-type="Major-subject-area"><kwd>Microbiology and infectious disease</kwd></kwd-group><kwd-group><kwd>platelets</kwd><kwd>dengue</kwd><kwd>thrombocytopenia</kwd></kwd-group><funding-group><award-group><funding-source>National Institutes of Health</funding-source><award-id>GM18458</award-id><principal-award-recipient>Author name(s)</principal-award-recipient></award-group><funding-statement>The funding sources were not involved in study design; collection, analysis, and interpretation of data; writing the article; and/or the decision to submit to the journal</funding-statement></funding-group></article-meta></front><body><sec sec-type="intro"><title>Introduction</title><p>Dengue is globally the most important arboviral infection and threatens an estimated 2.5 billion people worldwide <xref ref-type="bibr" rid="bib1">[1]</xref>. Thrombocytopenia is almost universally observed in dengue infection<xref ref-type="bibr" rid="bib2">[2]</xref>. This results from both reduced production and increased destruction of platelets<xref ref-type="bibr" rid="bib3">[3]</xref>-<xref ref-type="bibr" rid="bib5">[5]</xref>. It is thought that severe thrombocytopenia correlates with disease severity and may contribute to the risk of developing haemorrhage<xref ref-type="bibr" rid="bib6">[6]</xref>,<xref ref-type="bibr" rid="bib7">[7]</xref>. The 2009 WHO dengue guidelines do not advocate the use of prophylactic platelet transfusions, whereas the 2011 regional WHO guidelines for South East Asia suggest prophylactic platelets may be considered in those with a platelet count less than 10&#xD7;10<sup>9</sup>/L<xref ref-type="bibr" rid="bib8">[8]</xref>,<xref ref-type="bibr" rid="bib9">[9]</xref>. Some dengue-endemic countries support the use of prophylactic platelet transfusions to prevent haemorrhage in patients with thrombocytopenia, for example India (&lt;10&#xD7;10<sup>9</sup>/L), whereas others, such as Brazil, do not<xref ref-type="bibr" rid="bib10">[10]</xref>,<xref ref-type="bibr" rid="bib11">[11]</xref>. However platelet transfusions are costly, potentially dangerous and their use in dengue lacks an evidence base<xref ref-type="bibr" rid="bib12">[12]</xref>-<xref ref-type="bibr" rid="bib15">[15]</xref>.</p></sec><sec sec-type="methods"><title>Methods</title><p>We conducted a survey among physicians directly involved in the care of dengue patients in order to determine how platelets are used in the clinical management of dengue. The majority of respondents were practicing physicians in dengue-endemic areas. The exceptions to this were respondents from Africa, where dengue is emerging, and the UK where the respondents were infectious disease physicians who regularly see patients who have recently travelled to dengue-endemic areas. A questionnaire containing nine case histories and an additional question about prophylactic platelet transfusion thresholds was emailed to physicians with experience in managing dengue patients and known to us. Respondents were specifically asked that their responses reflect what they would do if they were the treating physician. Email recipients were invited to further disseminate the questionnaire within their own clinical networks. The complete list of questions is available as a supplementary file (<ext-link ext-link-type="uri" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://elife.org/lookup/suppl/doi:10.7554/eLife.000536.s001">Questionnaire S1</ext-link>).</p><p>The case histories were based on real clinical cases seen at the Hospital for Tropical Diseases in Ho Chi Minh City, Vietnam. Four case histories describe patients with clinically non-severe dengue but varying levels of thrombocytopenia. Case 1 describes an 18-year-old female with platelets of 23&#xD7;10<sup>9</sup>/L and no bleeding. Case 2 describes a 28-year-old male with platelets of 29&#xD7;10<sup>9</sup>/L. He had no bleeding but a past history of a perforated peptic ulcer. Case 3 describes a 29-year-old female with a rapid fall in platelets to 22&#xD7;10<sup>9</sup>/L. She had no bleeding. Case 4 describes a 30-year-old male with platelets of 3&#xD7;10<sup>9</sup>/L and no bleeding. Five case histories describe patients with different manifestations of severe dengue associated with varying levels of thrombocytopenia. Case 5 describes a 19-year-old male with platelets of 18&#xD7;10<sup>9</sup>/L. He had dengue hepatitis but no bleeding. Case 6 describes a 20-year-old female with platelets of 17&#xD7;10<sup>9</sup>/L. She had suspected dengue encephalitis but no bleeding. Case 7 describes a 24-year-old male with platelets of 31&#xD7;10<sup>9</sup>/L. He had hepatic failure thought to be secondary to dengue but no bleeding. Case 8 describes a 23-year-old female with platelets of 8&#xD7;10<sup>9</sup>/L. She had shock, epistaxis and vaginal bleeding. Case 9 describes a 23-year-old male with platelets of 33&#xD7;10<sup>9</sup>/L. He had shock and mucosal bleeding. The final question aimed to determine thresholds at which a physician would consider transfusing platelets as prophylaxis against haemorrhage. Respondents were asked to select a single option.</p></sec><sec sec-type="results"><title>Results</title><p>In total, 306 physicians from 20 different countries responded within a specified time period. The responses from Asia were 52 from Indonesia, 7 from Bangladesh, 5 from the Philippines, 9 from Singapore, 8 from Cambodia, 18 from Malaysia, 3 from Thailand, 20 from Vietnam and 12 from India. The responses from Latin America and the Caribbean were 13 from Cuba, 10 from Brazil, 17 from Paraguay, 6 from Peru, 1 from Mexico, 1 from Bolivia, 1 from Martinique and 81 from Colombia. The responses from Africa were 37 from Nigeria and 2 from South Africa. In addition there were 3 responses from the UK.</p><p>Among the 4 case histories describing patients with clinically non-severe dengue associated with varying levels of thrombocytopenia, 16-24% of respondents recommended platelet transfusion at platelet concentrations of 22-29&#xD7;10<sup>9</sup>/L., but approximately one-third of the respondents would transfuse platelets if the count fell to 3&#xD7;10<sup>9</sup>/L. (<xref ref-type="table" rid="tbl1">Table 1</xref>)</p><table-wrap id="tbl1" position="float"><object-id pub-id-type="doi">10.7554/eLife.000536.t001</object-id><label>Table 1</label><caption><title>Proportion of respondents choosing to transfuse platelets stratified by geographic region (n, (%)); BP = blood pressure; HR = heart rate; HCT = haematocrit.</title></caption><table><thead><tr><td>Clinical case</td><td align="char" char="(">Asia (n = 134)</td><td align="char" char="(">Africa (n = 39)</td><td align="char" char="(">S. America &amp; Caribbean (n = 130)</td><td align="char" char="(">UK (n = 3)</td><td align="char" char="(">Total (n = 306)</td></tr></thead><tbody><tr><td><bold>Case 1</bold> 18-year-old female; platelets 23&#xD7;10<sup>9</sup>/L; no haemorrhage; BP 120/80; HR 105; HCT 39%</td><td align="char" char="(">12 (9)</td><td align="char" char="(">38 (97.4)</td><td align="char" char="(">8 (6.2)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">58 (19)</td></tr><tr><td><bold>Case 2</bold> 28-year-old male; platelets 29&#xD7;10<sup>9</sup>/L; no haemorrhage; past history of perforated gastric ulcer; BP 100/75; HR 92; HCT 42%3</td><td align="char" char="(">20 (14.9)</td><td align="char" char="(">39 (100)</td><td align="char" char="(">13 (10)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">72 (23.5)</td></tr><tr><td><bold>Case 3</bold> 29-year-old female; rapid fall in platelets to 22&#xD7;10<sup>9</sup>/L; no haemorrhage; haemodynamically stable</td><td align="char" char="(">12 (9)</td><td align="char" char="(">30 (76.9)</td><td align="char" char="(">6 (4.6)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">48 (15.7)</td></tr><tr><td><bold>Case 4</bold> 30-year-old male; platelets 3&#xD7;10<sup>9</sup>/L; no haemorrhage; haemodynamically stable</td><td align="char" char="(">57 (42.5)</td><td align="char" char="(">37 (94.9)</td><td align="char" char="(">23 (17.7)</td><td align="char" char="(">3 (100)</td><td align="char" char="(">120 (39.2)</td></tr><tr><td><bold>Case 5</bold> 19-year-old male; platelets 18&#xD7;10<sup>9</sup>/L; dengue hepatitis; no haemorrhage; BP 90/60; HR 120; HCT 47%</td><td align="char" char="(">11 (8.2)</td><td align="char" char="(">36 (92.3)</td><td align="char" char="(">7 (5.4)</td><td align="char" char="(">2 (66.7)</td><td align="char" char="(">56 (18.3)</td></tr><tr><td><bold>Case 6</bold> 20-year-old female; platelets 17&#xD7;10<sup>9</sup>/L; dengue encephalitis; no haemorrhage; BP 100/70; HR 100; HCT 40%</td><td align="char" char="(">25 (18.7)</td><td align="char" char="(">39 (100)</td><td align="char" char="(">19 (14.6)</td><td align="char" char="(">1 (33.3)</td><td align="char" char="(">84 (27.5)</td></tr><tr><td><bold>Case 7</bold> 24-year-old male; platelets 31&#xD7;10<sup>9</sup>/L; hepatic failure secondary to dengue; no haemorrhage; BP 125/70; HR 110; HCT 42%</td><td align="char" char="(">5 (3.7)</td><td align="char" char="(">39 (100)</td><td align="char" char="(">9 (6.9)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">53 (17.3)</td></tr><tr><td><bold>Case 8</bold> 23-year-old female; platelets 8&#xD7;10<sup>9</sup>/L; shock, epistaxis and vaginal bleeding; BP 75/50; HR 110; HCT 42%</td><td align="char" char="(">86 (64.2)</td><td align="char" char="(">39 (100)</td><td align="char" char="(">43 (33.1)</td><td align="char" char="(">3 (100)</td><td align="char" char="(">171 (55.9)</td></tr><tr><td><bold>Case 9</bold> 23-year-old male; platelets 33&#xD7;10<sup>9</sup>/L; shock and mucosal bleeding; BP 70/50; HR 120; HCT 46%</td><td align="char" char="(">57 (42.5)</td><td align="char" char="(">39 (100)</td><td align="char" char="(">26 (20)</td><td align="char" char="(">1 (33.3)</td><td align="char" char="(">123 (40.2)</td></tr><tr><td><bold>Prophylactic platelet transfusion threshold:</bold></td><td/><td/><td/><td/><td/></tr><tr><td>&emsp;&emsp;&emsp;&emsp;&lt;50&#xD7;10<sup>9</sup>/L</td><td align="char" char="(">8 (6)</td><td align="char" char="(">23 (59)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">31 (10.1)</td></tr><tr><td>&emsp;&emsp;&emsp;&emsp;&lt;40&#xD7;10<sup>9</sup>/L</td><td align="char" char="(">1 (0.7)</td><td align="char" char="(">7 (17.9)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">8 (2.6)</td></tr><tr><td>&emsp;&emsp;&emsp;&emsp;&lt;30&#xD7;10<sup>9</sup>/L</td><td align="char" char="(">1 (0.7)</td><td align="char" char="(">7 (17.9)</td><td align="char" char="(">2 (1.5)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">10 (3.3)</td></tr><tr><td>&emsp;&emsp;&emsp;&emsp;&lt;20&#xD7;10<sup>9</sup>/L</td><td align="char" char="(">12 (9)</td><td align="char" char="(">1 (2.6)</td><td align="char" char="(">2 (1.5)</td><td align="char" char="(">2 (66.7)</td><td align="char" char="(">17 (5.6)</td></tr><tr><td>&emsp;&emsp;&emsp;&emsp;&lt;10&#xD7;10<sup>9</sup>/L</td><td align="char" char="(">33 (24.6)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">12 (9.2)</td><td align="char" char="(">1 (33.3)</td><td align="char" char="(">46 (15)</td></tr><tr><td>&emsp;&emsp;&emsp;&emsp;Not in absence of bleeding</td><td align="char" char="(">75 (56)</td><td align="char" char="(">1 (2.6)</td><td align="char" char="(">39 (30)</td><td align="char" char="(">0 (0)</td><td align="char" char="(">190 (62.1)</td></tr></tbody></table></table-wrap><p>Among the 5 case histories describing patients with different manifestations of severe dengue associated with varying levels of thrombocytopenia, more respondents would transfuse platelets if the patient was in shock and bleeding (case histories 8 and 9). There were substantial differences in the responses from physicians in Africa than those from Asia and America for all 9 cases (<xref ref-type="table" rid="tbl1">Table 1</xref>).</p><p>The final question aimed to determine thresholds at which a physician would consider transfusing platelets as prophylaxis against haemorrhage. Respondents were asked to select a single option. 31 (10%) respondents would consider a prophylactic platelet transfusion if the platelet count was below 50&#xD7;10<sup>9</sup>/L. 8 (2.6%) respondents would consider a prophylactic platelet transfusion if the platelet count was below 40&#xD7;10<sup>9</sup>. 10 (3.3%) respondents would consider a prophylactic platelet transfusion if the platelet count was below 30&#xD7;10<sup>9</sup>. 17 (5.6%) respondents would consider a prophylactic platelet transfusion if the platelet count was below 20&#xD7;10<sup>9</sup>. 46 (15%) respondents would consider a prophylactic platelet transfusion if the platelet count was below 10&#xD7;10<sup>9</sup>. 190 (62%) respondents would only consider transfusing platelets in patients with signs of haemorrhage.</p><p>The responses categorised by global region are summarised in<xref ref-type="table" rid="tbl1">Table 1</xref>.</p></sec><sec sec-type="discussion"><title>Discussion</title><p>Our study has limitations. There is an element of selection bias in the way the survey was conducted, as the physicians who distributed the survey within their countries were known to have an interest in dengue. The survey is subject to response bias meaning that the answers may not accurately reflect clinical practice in the respective countries. In addition, the country representation is not balanced.</p><p>Despite these limitations the striking result of this survey is the heterogeneity of approaches to the use of prophylactic platelet transfusions in dengue. 112/306 respondents would consider transfusing platelets prophylactically at various levels of thrombocytopenia. When the responses are categorised by region (<xref ref-type="table" rid="tbl1">Table 1</xref>) African respondents would advocate platelet transfusions more frequently, perhaps reflecting more limited experience with dengue and experience with other haemorrhagic fevers. The choice to use prophylactic platelet transfusions may be influenced by cost and availability of platelets, as well as individual experience in managing dengue and other medical conditions that affect the platelet count. There is considerable variability within countries suggesting an individual's practice may differ from recommendations in guidelines. For example 6/12 Indian respondents and 7/10 Brazilian respondents would consider the use of prophylactic platelets. The responses reflect wide variation in clinical practice and are indicative of the paucity of clinical evidence to guide practice in this area.</p><p>At present there is limited evidence to support the use of prophylactic platelet transfusions in dengue despite their inclusion in some national guidelines. As the global reach of dengue continues to expand the need to conduct clinical trials to construct an evidence base to guide the appropriate use of platelets in dengue becomes ever more pressing.</p></sec><sec><title>Supporting Information</title><p><bold><ext-link ext-link-type="uri" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://elife.org/lookup/suppl/doi:10.7554/eLife.000536.s001">Questionnaire S1 Dengue clinical scenarios</ext-link>.</bold> (DOC)</p></sec></body><back><ack><p>The authors would like to thank Dr Osvaldo Castro from IPK in Cuba for his assistance in distributing the questionnaires.</p></ack><fn-group><fn fn-type="conflict"><label>Competing interests</label><p>The authors have declared that no competing interests exist.</p></fn></fn-group><ref-list><title>References</title><ref id="bib1"><label>1.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Guzman</surname><given-names>MG</given-names></name><name><surname>Halstead</surname><given-names>SB</given-names></name><name><surname>Artsob</surname><given-names>H</given-names></name><name><surname>Buchy</surname><given-names>P</given-names></name><name><surname>Farrar</surname><given-names>J</given-names></name><etal/></person-group> (<year>2010</year>) <article-title>Dengue: a continuing global threat</article-title>. <source>Nat Rev Microbiol</source> <volume>8</volume>: <fpage>S7</fpage>&#x2013;<lpage>S16</lpage>.</mixed-citation></ref><ref id="bib2"><label>2.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Lee</surname><given-names>VJ</given-names></name><name><surname>Lye</surname><given-names>DC</given-names></name><name><surname>Sun</surname><given-names>Y</given-names></name><name><surname>Fernandez</surname><given-names>G</given-names></name><name><surname>Ong</surname><given-names>A</given-names></name><etal/></person-group> (<year>2008</year>) <article-title>Predictive value of simple clinical and laboratory variables for dengue hemorrhagic fever in adults</article-title>. <source>J Clin Virol</source> <volume>42</volume>: <fpage>34</fpage>&#x2013;<lpage>39</lpage></mixed-citation></ref><ref id="bib3"><label>3.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>La Russa</surname><given-names>VF</given-names></name><name><surname>Innis</surname><given-names>BL</given-names></name></person-group> (<year>1995</year>) <article-title>Mechanisms of dengue virus-induced bone marrow suppression</article-title>. <source>Baillieres Clin Haematol</source> <volume>8</volume>: <fpage>249</fpage>&#x2013;<lpage>270</lpage></mixed-citation></ref><ref id="bib4"><label>4.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Lei</surname><given-names>HY</given-names></name><name><surname>Yeh</surname><given-names>TM</given-names></name><name><surname>Liu</surname><given-names>HS</given-names></name><name><surname>Lin</surname><given-names>YS</given-names></name><name><surname>Chen</surname><given-names>SH</given-names></name><etal/></person-group> (<year>2001</year>) <article-title>Immunopathogenesis of dengue virus infection</article-title>. <source>J Biomed Sci</source> <volume>8</volume>: <fpage>377</fpage>&#x2013;<lpage>388</lpage></mixed-citation></ref><ref id="bib5"><label>5.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Alonzo</surname><given-names>MT</given-names></name><name><surname>Lacuesta</surname><given-names>TL</given-names></name><name><surname>Dimaano</surname><given-names>EM</given-names></name><name><surname>Kurosu</surname><given-names>T</given-names></name><name><surname>Suarez</surname><given-names>LA</given-names></name><etal/></person-group> (<year>2012</year>) <article-title>Platelet apoptosis and apoptotic platelet clearance by macrophages in secondary dengue virus infections</article-title>. <source>J Infect Dis</source> <volume>205</volume>: <fpage>1321</fpage>&#x2013;<lpage>1329</lpage></mixed-citation></ref><ref id="bib6"><label>6.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Krishnamurti</surname><given-names>C</given-names></name><name><surname>Kalayanarooj</surname><given-names>S</given-names></name><name><surname>Cutting</surname><given-names>MA</given-names></name><name><surname>Peat</surname><given-names>RA</given-names></name><name><surname>Rothwell</surname><given-names>SW</given-names></name><etal/></person-group> (<year>2001</year>) <article-title>Mechanisms of hemorrhage in dengue without circulatory collapse</article-title>. <source>Am J Trop Med Hyg</source> <volume>65</volume>: <fpage>840</fpage>&#x2013;<lpage>847</lpage></mixed-citation></ref><ref id="bib7"><label>7.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Noisakran</surname><given-names>S</given-names></name><name><surname>Chokephaibulkit</surname><given-names>K</given-names></name><name><surname>Songprakhon</surname><given-names>P</given-names></name><name><surname>Onlamoon</surname><given-names>N</given-names></name><name><surname>Hsiao</surname><given-names>HM</given-names></name><etal/></person-group> (<year>2009</year>) <article-title>A re-evaluation of the mechanisms leading to dengue hemorrhagic fever</article-title>. <source>Ann N Y Acad Sci</source> <volume>1171</volume>: <fpage>E24</fpage>&#x2013;<lpage>35</lpage></mixed-citation></ref><ref id="bib8"><label>8.</label><mixed-citation publication-type="book"><collab>WHO</collab> (<year>2009</year>) <source>Dengue: guidelines for diagnosis, treatment, prevention and control - New edition</source>. <publisher-loc>Geneva</publisher-loc>: <publisher-name>World Health Organisation</publisher-name>.</mixed-citation></ref><ref id="bib9"><label>9.</label><mixed-citation publication-type="other"><collab>WHO</collab> (<year>2011</year>) <article-title>Comprehensive guidelines for the prevention and control of dengue and dengue haemorrhagic fever, revised and expanded edition</article-title>.. In: Asia ROfS-E, editor. Delhi.</mixed-citation></ref><ref id="bib10"><label>10.</label><mixed-citation publication-type="other"><person-group person-group-type="author"><name><surname>India</surname><given-names>Go</given-names></name></person-group> (<year>2008</year>) <article-title>Guidelines for clinical management of dengue fever, dengue haemorrhagic fever and dengue shock syndrome</article-title>. In: Programme DoNVBDC, editor. Delhi.</mixed-citation></ref><ref id="bib11"><label>11.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Verdeal</surname><given-names>J</given-names></name><name><surname>Filho</surname><given-names>RC</given-names></name><name><surname>Vanzillotta</surname><given-names>C</given-names></name><name><surname>Macedo</surname><given-names>G</given-names></name><name><surname>Bozza</surname><given-names>F</given-names></name><etal/></person-group> (<year>2011</year>) <article-title>Guidelines for the management of patients with severe forms of dengue</article-title>. <source>Rev Bras Ter Intensiva</source> <volume>23</volume>: <fpage>125</fpage>&#x2013;<lpage>133</lpage></mixed-citation></ref><ref id="bib12"><label>12.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Lum</surname><given-names>LC</given-names></name><name><surname>Abdel-Latif Mel</surname><given-names>A</given-names></name><name><surname>Goh</surname><given-names>AY</given-names></name><name><surname>Chan</surname><given-names>PW</given-names></name><name><surname>Lam</surname><given-names>SK</given-names></name></person-group> (<year>2003</year>) <article-title>Preventive transfusion in Dengue shock syndrome-is it necessary?</article-title> <source>J Pediatr</source> <volume>143</volume>: <fpage>682</fpage>&#x2013;<lpage>684</lpage></mixed-citation></ref><ref id="bib13"><label>13.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Lye</surname><given-names>DC</given-names></name><name><surname>Lee</surname><given-names>VJ</given-names></name><name><surname>Sun</surname><given-names>Y</given-names></name><name><surname>Leo</surname><given-names>YS</given-names></name></person-group> (<year>2009</year>) <article-title>Lack of efficacy of prophylactic platelet transfusion for severe thrombocytopenia in adults with acute uncomplicated dengue infection</article-title>. <source>Clin Infect Dis</source> <volume>48</volume>: <fpage>1262</fpage>&#x2013;<lpage>1265</lpage></mixed-citation></ref><ref id="bib14"><label>14.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Kurukularatne</surname><given-names>C</given-names></name><name><surname>Dimatatac</surname><given-names>F</given-names></name><name><surname>Teo</surname><given-names>DL</given-names></name><name><surname>Lye</surname><given-names>DC</given-names></name><name><surname>Leo</surname><given-names>YS</given-names></name></person-group> (<year>2011</year>) <article-title>When less is more: can we abandon prophylactic platelet transfusion in Dengue fever?</article-title><source>Ann Acad Med Singapore</source> <volume>40</volume>: <fpage>539</fpage>&#x2013;<lpage>537</lpage></mixed-citation></ref><ref id="bib15"><label>15.</label><mixed-citation publication-type="journal"><person-group person-group-type="author"><name><surname>Sharma</surname><given-names>A</given-names></name><name><surname>Charles</surname><given-names>K</given-names></name><name><surname>Chadee</surname><given-names>D</given-names></name><name><surname>Teelucksingh</surname><given-names>S</given-names></name></person-group> (<year>2012</year>) <article-title>Dengue hemorrhagic Fever in trinidad and tobago: a case for a conservative approach to platelet transfusion</article-title>. <source>Am J Trop Med Hyg</source> <volume>86</volume>: <fpage>531</fpage>&#x2013;<lpage>535</lpage></mixed-citation></ref></ref-list></back></article>"""},

             
            }
          ]
        ]
      }
    },

		# 1
    {'obj': '2341349f-641a-4b61-9e7d-3e7b1b81bebd',
		 'key': 'ref/ref',
		 'ref/ref': 'Guzman MG, Halstead SB, Artsob H, Buchy P, Farrar J, et al. (2010) Dengue: a continuing global threat. Nat Rev Microbiol 8: S7&#x2013;S16.',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Guzman MG, Halstead SB, Artsob H, Buchy P, Farrar J, et al. (2010) Dengue: a continuing global threat. Nat Rev Microbiol 8: S7&#x2013;S16."',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Guzman MG, Halstead SB, Artsob H, Buchy P, Farrar J, et al. (2010) Dengue: a continuing global threat. Nat Rev Microbiol 8: S7&#x2013;S16.'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Dengue: a continuing global threat'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Guzman MG, Halstead SB, Artsob H, Buchy P, Farrar J, et al.'},
             settings.namespace + '/' + 'ref/year': {'value': '2010'},
             settings.namespace + '/' + 'ref/source': {'value': 'Nat Rev Microbiol'},
             settings.namespace + '/' + 'ref/volume': {'value': '8'},
             settings.namespace + '/' + 'ref/fpage': {'value': 'S7'},
             settings.namespace + '/' + 'ref/lpage': {'value': 'S16'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},
		
		# 2
    {'obj': '5bbff29a-eae4-4add-b5ba-9d834da3eeb9',
		 'key': 'ref/ref',
		 'ref/ref': 'Lee VJ, Lye DC, Sun Y, Fernandez G, Ong A, et al. (2008) Predictive value of simple clinical and laboratory variables for dengue hemorrhagic fever in adults. J Clin Virol 42: 34&#x2013;39',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Lee VJ, Lye DC, Sun Y, Fernandez G, Ong A, et al. (2008) Predictive value of simple clinical and laboratory variables for dengue hemorrhagic fever in adults. J Clin Virol 42: 34&#x2013;39"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Lee VJ, Lye DC, Sun Y, Fernandez G, Ong A, et al. (2008) Predictive value of simple clinical and laboratory variables for dengue hemorrhagic fever in adults. J Clin Virol 42: 34&#x2013;39'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Predictive value of simple clinical and laboratory variables for dengue hemorrhagic fever in adults'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Lee VJ, Lye DC, Sun Y, Fernandez G, Ong A, et al.'},
             settings.namespace + '/' + 'ref/year': {'value': '2008'},
             settings.namespace + '/' + 'ref/source': {'value': 'J Clin Virol'},
             settings.namespace + '/' + 'ref/volume': {'value': '42'},
             settings.namespace + '/' + 'ref/fpage': {'value': '34'},
             settings.namespace + '/' + 'ref/lpage': {'value': '39'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},
		
		# 3
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'La Russa VF, Innis BL (1995) Mechanisms of dengue virus-induced bone marrow suppression. Baillieres Clin Haematol 8: 249&#x2013;270',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "La Russa VF, Innis BL (1995) Mechanisms of dengue virus-induced bone marrow suppression. Baillieres Clin Haematol 8: 249&#x2013;270"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'La Russa VF, Innis BL (1995) Mechanisms of dengue virus-induced bone marrow suppression. Baillieres Clin Haematol 8: 249&#x2013;270'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Mechanisms of dengue virus-induced bone marrow suppression'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'La Russa VF, Innis BL'},
             settings.namespace + '/' + 'ref/year': {'value': '1995'},
             settings.namespace + '/' + 'ref/source': {'value': 'Baillieres Clin Haematol'},
             settings.namespace + '/' + 'ref/volume': {'value': '8'},
             settings.namespace + '/' + 'ref/fpage': {'value': '249'},
             settings.namespace + '/' + 'ref/lpage': {'value': '270'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 4
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'Lei HY, Yeh TM, Liu HS, Lin YS, Chen SH, et al. (2001) Immunopathogenesis of dengue virus infection. J Biomed Sci 8: 377&#x2013;388',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Lei HY, Yeh TM, Liu HS, Lin YS, Chen SH, et al. (2001) Immunopathogenesis of dengue virus infection. J Biomed Sci 8: 377&#x2013;388"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Lei HY, Yeh TM, Liu HS, Lin YS, Chen SH, et al. (2001) Immunopathogenesis of dengue virus infection. J Biomed Sci 8: 377&#x2013;388'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Immunopathogenesis of dengue virus infection'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Lei HY, Yeh TM, Liu HS, Lin YS, Chen SH, et al.'},
             settings.namespace + '/' + 'ref/year': {'value': '2001'},
             settings.namespace + '/' + 'ref/source': {'value': 'J Biomed Sci'},
             settings.namespace + '/' + 'ref/volume': {'value': '8'},
             settings.namespace + '/' + 'ref/fpage': {'value': '377'},
             settings.namespace + '/' + 'ref/lpage': {'value': '388'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 5
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'Alonzo MT, Lacuesta TL, Dimaano EM, Kurosu T, Suarez LA, et al. (2012) Platelet apoptosis and apoptotic platelet clearance by macrophages in secondary dengue virus infections. J Infect Dis 205: 1321&#x2013;1329',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Alonzo MT, Lacuesta TL, Dimaano EM, Kurosu T, Suarez LA, et al. (2012) Platelet apoptosis and apoptotic platelet clearance by macrophages in secondary dengue virus infections. J Infect Dis 205: 1321&#x2013;1329"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Alonzo MT, Lacuesta TL, Dimaano EM, Kurosu T, Suarez LA, et al. (2012) Platelet apoptosis and apoptotic platelet clearance by macrophages in secondary dengue virus infections. J Infect Dis 205: 1321&#x2013;1329'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Platelet apoptosis and apoptotic platelet clearance by macrophages in secondary dengue virus infections'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Alonzo MT, Lacuesta TL, Dimaano EM, Kurosu T, Suarez LA, et al.'},
             settings.namespace + '/' + 'ref/year': {'value': '2012'},
             settings.namespace + '/' + 'ref/source': {'value': 'J Infect Dis'},
             settings.namespace + '/' + 'ref/volume': {'value': '205'},
             settings.namespace + '/' + 'ref/fpage': {'value': '1321'},
             settings.namespace + '/' + 'ref/lpage': {'value': '1329'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 6
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'Krishnamurti C, Kalayanarooj S, Cutting MA, Peat RA, Rothwell SW, et al. (2001) Mechanisms of hemorrhage in dengue without circulatory collapse. Am J Trop Med Hyg 65: 840&#x2013;847',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Krishnamurti C, Kalayanarooj S, Cutting MA, Peat RA, Rothwell SW, et al. (2001) Mechanisms of hemorrhage in dengue without circulatory collapse. Am J Trop Med Hyg 65: 840&#x2013;847"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Krishnamurti C, Kalayanarooj S, Cutting MA, Peat RA, Rothwell SW, et al. (2001) Mechanisms of hemorrhage in dengue without circulatory collapse. Am J Trop Med Hyg 65: 840&#x2013;847'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Mechanisms of hemorrhage in dengue without circulatory collapse'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Krishnamurti C, Kalayanarooj S, Cutting MA, Peat RA, Rothwell SW, et al.'},
             settings.namespace + '/' + 'ref/year': {'value': '2001'},
             settings.namespace + '/' + 'ref/source': {'value': 'Am J Trop Med Hyg'},
             settings.namespace + '/' + 'ref/volume': {'value': '65'},
             settings.namespace + '/' + 'ref/fpage': {'value': '840'},
             settings.namespace + '/' + 'ref/lpage': {'value': '847'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 7
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'Noisakran S, Chokephaibulkit K, Songprakhon P, Onlamoon N, Hsiao HM, et al. (2009) A re-evaluation of the mechanisms leading to dengue hemorrhagic fever. Ann N Y Acad Sci 1171: E24&#x2013;35',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Noisakran S, Chokephaibulkit K, Songprakhon P, Onlamoon N, Hsiao HM, et al. (2009) A re-evaluation of the mechanisms leading to dengue hemorrhagic fever. Ann N Y Acad Sci 1171: E24&#x2013;35"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Noisakran S, Chokephaibulkit K, Songprakhon P, Onlamoon N, Hsiao HM, et al. (2009) A re-evaluation of the mechanisms leading to dengue hemorrhagic fever. Ann N Y Acad Sci 1171: E24&#x2013;35'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'A re-evaluation of the mechanisms leading to dengue hemorrhagic fever'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Noisakran S, Chokephaibulkit K, Songprakhon P, Onlamoon N, Hsiao HM, et al.'},
             settings.namespace + '/' + 'ref/year': {'value': '2009'},
             settings.namespace + '/' + 'ref/source': {'value': 'Ann N Y Acad Sci'},
             settings.namespace + '/' + 'ref/volume': {'value': '1171'},
             settings.namespace + '/' + 'ref/fpage': {'value': 'E24'},
             settings.namespace + '/' + 'ref/lpage': {'value': '35'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 8
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'WHO (2009) Dengue: guidelines for diagnosis, treatment, prevention and control - New edition. Geneva: World Health Organisation.',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "WHO (2009) Dengue: guidelines for diagnosis, treatment, prevention and control - New edition. Geneva: World Health Organisation."',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'WHO (2009) Dengue: guidelines for diagnosis, treatment, prevention and control - New edition. Geneva: World Health Organisation.'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Dengue: guidelines for diagnosis, treatment, prevention and control - New edition'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'book'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/authors': {'value': '________________________'},
             settings.namespace + '/' + 'ref/year': {'value': '2009'},
             #settings.namespace + '/' + 'ref/source': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/volume': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/fpage': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/lpage': {'value': '________________________'},
             settings.namespace + '/' + 'ref/collab': {'value': 'WHO'},
             settings.namespace + '/' + 'ref/publisher_loc': {'value': 'Geneva'},
             settings.namespace + '/' + 'ref/publisher_name': {'value': 'World Health Organisation'},
						}
					]
				]
			}
		},		
		# 9
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'WHO (2011) Comprehensive guidelines for the prevention and control of dengue and dengue haemorrhagic fever, revised and expanded edition.. In: Asia ROfS-E, editor. Delhi.',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "WHO (2011) Comprehensive guidelines for the prevention and control of dengue and dengue haemorrhagic fever, revised and expanded edition.. In: Asia ROfS-E, editor. Delhi."',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'WHO (2011) Comprehensive guidelines for the prevention and control of dengue and dengue haemorrhagic fever, revised and expanded edition.. In: Asia ROfS-E, editor. Delhi.'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Comprehensive guidelines for the prevention and control of dengue and dengue haemorrhagic fever, revised and expanded edition'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'book'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/authors': {'value': '________________________'},
             settings.namespace + '/' + 'ref/year': {'value': '2011'},
             #settings.namespace + '/' + 'ref/source': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/volume': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/fpage': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/lpage': {'value': '________________________'},
             settings.namespace + '/' + 'ref/collab': {'value': 'WHO'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 10
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'India Go (2008) Guidelines for clinical management of dengue fever, dengue haemorrhagic fever and dengue shock syndrome. In: Programme DoNVBDC, editor. Delhi.',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "India Go (2008) Guidelines for clinical management of dengue fever, dengue haemorrhagic fever and dengue shock syndrome. In: Programme DoNVBDC, editor. Delhi."',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'India Go (2008) Guidelines for clinical management of dengue fever, dengue haemorrhagic fever and dengue shock syndrome. In: Programme DoNVBDC, editor. Delhi.'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Guidelines for clinical management of dengue fever, dengue haemorrhagic fever and dengue shock syndrome'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'other'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'India Go'},
             settings.namespace + '/' + 'ref/year': {'value': '2008'},
             #settings.namespace + '/' + 'ref/source': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/volume': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/fpage': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/lpage': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 11
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'Verdeal J, Filho RC, Vanzillotta C, Macedo G, Bozza F, et al. (2011) Guidelines for the management of patients with severe forms of dengue. Rev Bras Ter Intensiva 23: 125&#x2013;133',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Verdeal J, Filho RC, Vanzillotta C, Macedo G, Bozza F, et al. (2011) Guidelines for the management of patients with severe forms of dengue. Rev Bras Ter Intensiva 23: 125&#x2013;133"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Verdeal J, Filho RC, Vanzillotta C, Macedo G, Bozza F, et al. (2011) Guidelines for the management of patients with severe forms of dengue. Rev Bras Ter Intensiva 23: 125&#x2013;133'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Guidelines for the management of patients with severe forms of dengue'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Verdeal J, Filho RC, Vanzillotta C, Macedo G, Bozza F, et al.'},
             settings.namespace + '/' + 'ref/year': {'value': '2011'},
             settings.namespace + '/' + 'ref/source': {'value': 'Rev Bras Ter Intensiva'},
             settings.namespace + '/' + 'ref/volume': {'value': '23'},
             settings.namespace + '/' + 'ref/fpage': {'value': '125'},
             settings.namespace + '/' + 'ref/lpage': {'value': '133'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 12
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'Lum LC, Abdel-Latif Mel A, Goh AY, Chan PW, Lam SK (2003) Preventive transfusion in Dengue shock syndrome-is it necessary? J Pediatr 143: 682&#x2013;684',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Lum LC, Abdel-Latif Mel A, Goh AY, Chan PW, Lam SK (2003) Preventive transfusion in Dengue shock syndrome-is it necessary? J Pediatr 143: 682&#x2013;684"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Lum LC, Abdel-Latif Mel A, Goh AY, Chan PW, Lam SK (2003) Preventive transfusion in Dengue shock syndrome-is it necessary? J Pediatr 143: 682&#x2013;684'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Preventive transfusion in Dengue shock syndrome-is it necessary?'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Lum LC, Abdel-Latif Mel A, Goh AY, Chan PW, Lam SK'},
             settings.namespace + '/' + 'ref/year': {'value': '2003'},
             settings.namespace + '/' + 'ref/source': {'value': 'J Pediatr'},
             settings.namespace + '/' + 'ref/volume': {'value': '143'},
             settings.namespace + '/' + 'ref/fpage': {'value': '682'},
             settings.namespace + '/' + 'ref/lpage': {'value': '684'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 13
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'Lye DC, Lee VJ, Sun Y, Leo YS (2009) Lack of efficacy of prophylactic platelet transfusion for severe thrombocytopenia in adults with acute uncomplicated dengue infection. Clin Infect Dis 48: 1262&#x2013;1265',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Lye DC, Lee VJ, Sun Y, Leo YS (2009) Lack of efficacy of prophylactic platelet transfusion for severe thrombocytopenia in adults with acute uncomplicated dengue infection. Clin Infect Dis 48: 1262&#x2013;1265"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Lye DC, Lee VJ, Sun Y, Leo YS (2009) Lack of efficacy of prophylactic platelet transfusion for severe thrombocytopenia in adults with acute uncomplicated dengue infection. Clin Infect Dis 48: 1262&#x2013;1265'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Lack of efficacy of prophylactic platelet transfusion for severe thrombocytopenia in adults with acute uncomplicated dengue infection'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Lye DC, Lee VJ, Sun Y, Leo YS'},
             settings.namespace + '/' + 'ref/year': {'value': '2009'},
             settings.namespace + '/' + 'ref/source': {'value': 'Clin Infect Dis'},
             settings.namespace + '/' + 'ref/volume': {'value': '48'},
             settings.namespace + '/' + 'ref/fpage': {'value': '1262'},
             settings.namespace + '/' + 'ref/lpage': {'value': '1265'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 14
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'Kurukularatne C, Dimatatac F, Teo DL, Lye DC, Leo YS (2011) When less is more: can we abandon prophylactic platelet transfusion in Dengue fever? Ann Acad Med Singapore 40: 539&#x2013;537',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Kurukularatne C, Dimatatac F, Teo DL, Lye DC, Leo YS (2011) When less is more: can we abandon prophylactic platelet transfusion in Dengue fever? Ann Acad Med Singapore 40: 539&#x2013;537"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Kurukularatne C, Dimatatac F, Teo DL, Lye DC, Leo YS (2011) When less is more: can we abandon prophylactic platelet transfusion in Dengue fever? Ann Acad Med Singapore 40: 539&#x2013;537'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'When less is more: can we abandon prophylactic platelet transfusion in Dengue fever?'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Kurukularatne C, Dimatatac F, Teo DL, Lye DC, Leo YS'},
             settings.namespace + '/' + 'ref/year': {'value': '2011'},
             settings.namespace + '/' + 'ref/source': {'value': 'Ann Acad Med Singapore'},
             settings.namespace + '/' + 'ref/volume': {'value': '40'},
             settings.namespace + '/' + 'ref/fpage': {'value': '539'},
             settings.namespace + '/' + 'ref/lpage': {'value': '537'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},		
		# 15
    {'obj': '',
		 'key': 'ref/ref',
		 'ref/ref': 'Sharma A, Charles K, Chadee D, Teelucksingh S (2012) Dengue hemorrhagic Fever in trinidad and tobago: a case for a conservative approach to platelet transfusion. Am J Trop Med Hyg 86: 531&#x2013;535',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'ref/ref = "Sharma A, Charles K, Chadee D, Teelucksingh S (2012) Dengue hemorrhagic Fever in trinidad and tobago: a case for a conservative approach to platelet transfusion. Am J Trop Med Hyg 86: 531&#x2013;535"',
            {
             settings.namespace + '/' + 'ref/ref': {'value': 'Sharma A, Charles K, Chadee D, Teelucksingh S (2012) Dengue hemorrhagic Fever in trinidad and tobago: a case for a conservative approach to platelet transfusion. Am J Trop Med Hyg 86: 531&#x2013;535'},
             settings.namespace + '/' + 'ref/article_title': {'value': 'Dengue hemorrhagic Fever in trinidad and tobago: a case for a conservative approach to platelet transfusion'},
             settings.namespace + '/' + 'ref/publication_type': {'value': 'journal'},
             #settings.namespace + '/' + 'ref/doi': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/pmid': {'value': '________________________'},
             settings.namespace + '/' + 'ref/authors': {'value': 'Sharma A, Charles K, Chadee D, Teelucksingh S'},
             settings.namespace + '/' + 'ref/year': {'value': '2012'},
             settings.namespace + '/' + 'ref/source': {'value': 'Am J Trop Med Hyg'},
             settings.namespace + '/' + 'ref/volume': {'value': '86'},
             settings.namespace + '/' + 'ref/fpage': {'value': '531'},
             settings.namespace + '/' + 'ref/lpage': {'value': '535'},
             #settings.namespace + '/' + 'ref/collab': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_loc': {'value': '________________________'},
             #settings.namespace + '/' + 'ref/publisher_name': {'value': '________________________'},
						}
					]
				]
			}
		},
		
		# Sample ALM data sources
    {'obj': '',
		 'key': 'alm_source/source',
		 'alm_source/source': 'highwire',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'alm_source/source = "highwire"',
            {
             settings.namespace + '/' + 'alm_source/url': {'value': 'http://highwire.org/'},
             settings.namespace + '/' + 'alm_source/name': {'value': 'HighWire'},
             settings.namespace + '/' + 'alm_source/trusted': {'value': True},
						}
					]
				]
			}
		},
		
    {'obj': '',
		 'key': 'alm_source/source',
		 'alm_source/source': 'total-impact',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'alm_source/source = "total-impact"',
            {
             settings.namespace + '/' + 'alm_source/url': {'value': 'http://total-impact.org/'},
             settings.namespace + '/' + 'alm_source/name': {'value': 'total-impact'},
             settings.namespace + '/' + 'alm_source/trusted': {'value': True},
						}
					]
				]
			}
		},
		
		# Sample (fake) ALM data - kludge: use concatenated values as a "key" for now
    {'obj': '',
		 'key': 'alm/temp_key',
		 'alm/temp_key': '10.7554/eLife.000536_pdf_month_August_2012',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'alm/temp_key = "10.7554/eLife.000536_pdf_month_August_2012"',
            {
             settings.namespace + '/' + 'alm/temp_key': {'value': '10.7554/eLife.000536_pdf_month_August_2012'},
             settings.namespace + '/' + 'alm/doi': {'value': '10.7554/eLife.000536'},
						 settings.namespace + '/' + 'alm/type': {'value': 'pdf'},
             settings.namespace + '/' + 'alm/source': {'value': 'highwire'},
             settings.namespace + '/' + 'alm/value': {'value': '10'},
             settings.namespace + '/' + 'alm/timespan': {'value': 'month'},
             settings.namespace + '/' + 'alm/date_date': {'value': 'August, 2012'},
             #settings.namespace + '/' + 'alm/date_day': {'value': '________________________'},
             settings.namespace + '/' + 'alm/date_month': {'value': '8'},
             settings.namespace + '/' + 'alm/date_year': {'value': '2012'},
             settings.namespace + '/' + 'alm/date_timestamp': {'value': '1343779200'},
             settings.namespace + '/' + 'alm/complete': {'value': False},
						}
					]
				]
			}
		},
		
    {'obj': '',
		 'key': 'alm/temp_key',
		 'alm/temp_key': '10.7554/eLife.000536_pdf_day_August_1_2012',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'alm/temp_key = "10.7554/eLife.000536_pdf_day_August_1_2012"',
            {
             settings.namespace + '/' + 'alm/temp_key': {'value': '10.7554/eLife.000536_pdf_day_August_1_2012'},
             settings.namespace + '/' + 'alm/doi': {'value': '10.7554/eLife.000536'},
						 settings.namespace + '/' + 'alm/type': {'value': 'pdf'},
             settings.namespace + '/' + 'alm/source': {'value': 'highwire'},
             settings.namespace + '/' + 'alm/value': {'value': '1'},
             settings.namespace + '/' + 'alm/timespan': {'value': 'day'},
             settings.namespace + '/' + 'alm/date_date': {'value': 'August 1, 2012'},
             settings.namespace + '/' + 'alm/date_day': {'value': '1'},
             settings.namespace + '/' + 'alm/date_month': {'value': '8'},
             settings.namespace + '/' + 'alm/date_year': {'value': '2012'},
             settings.namespace + '/' + 'alm/date_timestamp': {'value': '1343779200'},
             settings.namespace + '/' + 'alm/complete': {'value': True},
						}
					]
				]
			}
		},
		
    {'obj': '',
		 'key': 'alm/temp_key',
		 'alm/temp_key': '10.7554/eLife.000536_web_month_August_2012',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'alm/temp_key = "10.7554/eLife.000536_web_month_August_2012"',
            {
             settings.namespace + '/' + 'alm/temp_key': {'value': '10.7554/eLife.000536_web_month_August_2012'},
             settings.namespace + '/' + 'alm/doi': {'value': '10.7554/eLife.000536'},
						 settings.namespace + '/' + 'alm/type': {'value': 'web'},
             settings.namespace + '/' + 'alm/source': {'value': 'highwire'},
             settings.namespace + '/' + 'alm/value': {'value': '42'},
             settings.namespace + '/' + 'alm/timespan': {'value': 'month'},
             settings.namespace + '/' + 'alm/date_date': {'value': 'August, 2012'},
             #settings.namespace + '/' + 'alm/date_day': {'value': '________________________'},
             settings.namespace + '/' + 'alm/date_month': {'value': '8'},
             settings.namespace + '/' + 'alm/date_year': {'value': '2012'},
             settings.namespace + '/' + 'alm/date_timestamp': {'value': '1343779200'},
             settings.namespace + '/' + 'alm/complete': {'value': False},
						}
					]
				]
			}
		},
		
    {'obj': '',
		 'key': 'alm/temp_key',
		 'alm/temp_key': '10.7554/eLife.000536_web_year_2012',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'alm/temp_key = "10.7554/eLife.000536_web_year_2012"',
            {
             settings.namespace + '/' + 'alm/temp_key': {'value': '10.7554/eLife.000536_web_year_2012'},
             settings.namespace + '/' + 'alm/doi': {'value': '10.7554/eLife.000536'},
						 settings.namespace + '/' + 'alm/type': {'value': 'web'},
             settings.namespace + '/' + 'alm/source': {'value': 'highwire'},
             settings.namespace + '/' + 'alm/value': {'value': '420'},
             settings.namespace + '/' + 'alm/timespan': {'value': 'year'},
             settings.namespace + '/' + 'alm/date_date': {'value': '2012'},
             #settings.namespace + '/' + 'alm/date_day': {'value': '________________________'},
             #settings.namespace + '/' + 'alm/date_month': {'value': '8'},
             settings.namespace + '/' + 'alm/date_year': {'value': '2012'},
             settings.namespace + '/' + 'alm/date_timestamp': {'value': '1325376000'},
             settings.namespace + '/' + 'alm/complete': {'value': False},
						}
					]
				]
			}
		},
		
    {'obj': '',
		 'key': 'alm/temp_key',
		 'alm/temp_key': '10.7554/eLife.000536_web_total',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'alm/temp_key = "10.7554/eLife.000536_web_total"',
            {
             settings.namespace + '/' + 'alm/temp_key': {'value': '10.7554/eLife.000536_web_total'},
             settings.namespace + '/' + 'alm/doi': {'value': '10.7554/eLife.000536'},
						 settings.namespace + '/' + 'alm/type': {'value': 'web'},
             settings.namespace + '/' + 'alm/source': {'value': 'highwire'},
             settings.namespace + '/' + 'alm/value': {'value': '462'},
             settings.namespace + '/' + 'alm/timespan': {'value': 'total'},
             #settings.namespace + '/' + 'alm/date_date': {'value': '2012'},
             #settings.namespace + '/' + 'alm/date_day': {'value': '________________________'},
             #settings.namespace + '/' + 'alm/date_month': {'value': '8'},
             #settings.namespace + '/' + 'alm/date_year': {'value': '2012'},
             settings.namespace + '/' + 'alm/date_timestamp': {'value': '1346274182'},
             settings.namespace + '/' + 'alm/complete': {'value': True},
						}
					]
				]
			}
		},
		
    {'obj': '',
		 'key': 'alm/temp_key',
		 'alm/temp_key': '10.7554/eLife.000536_twitter_year_2012',
		 'query':
      {'queries':
        [
          [ settings.namespace + '/' + 'alm/temp_key = "10.7554/eLife.000536_twitter_year_2012"',
            {
             settings.namespace + '/' + 'alm/temp_key': {'value': '10.7554/eLife.000536_twitter_year_2012'},
             settings.namespace + '/' + 'alm/doi': {'value': '10.7554/eLife.000536'},
             settings.namespace + '/' + 'alm/type': {'value': 'twitter'},
             settings.namespace + '/' + 'alm/source': {'value': 'total-impact'},
             settings.namespace + '/' + 'alm/value': {'value': '8'},
             settings.namespace + '/' + 'alm/timespan': {'value': 'year'},
             settings.namespace + '/' + 'alm/date_date': {'value': '2012'},
             #settings.namespace + '/' + 'alm/date_day': {'value': '________________________'},
             #settings.namespace + '/' + 'alm/date_month': {'value': '8'},
             settings.namespace + '/' + 'alm/date_year': {'value': '2012'},
             settings.namespace + '/' + 'alm/date_timestamp': {'value': '1325376000'},
             settings.namespace + '/' + 'alm/complete': {'value': False},
						}
					]
				]
			}
		},
		
]