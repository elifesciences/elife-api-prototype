
Overview and Goals for the API

The goal of the eLife API is to provide access to information around eLife articles through an interface that has a low barrier of entry for developers. The API should also provide the ability for developers to add metadata of their own onto representations of eLife articles.  For launch in November the key goal is to provide metadata through the API. That metdata should provide links to full text XML, and to the underlying data that the paper references. Providing the full text and the full data from within the API data store is not deemed to be required. 

In order to achieve these goals we are considering using Fluidinfo, which will enable us to provide a RESTFUL JSON interface. It will also allow users of the API to decorate our objects with their own metadata. 

Overview of our data objects.

We can think of the metadata that we want to provision as coming from the following families; standard article, alt-metric, author. In addition we can consider the creation of composite queries across these categories. Below we will discuss some specific use cases from each of these categories, 


Sample Use Cases

Standard Metadata

Given I have the DOI, as a user I want to be able to GET the core article metatdata, where the core article metadata includes: 

title 
author list 
Subject area category
Article type
Publication information
Title
funding
Text book summary 1 comment
Received/revised/acceptance dates
Copyright
Keywords?
Contribution statement
Acknowledgements
Competing interests
Ethics approval
Linked articles
Trial registration number ICMJE recommend it is placed at the end of the abstract
Reporting guidelines Cited? Data suppl files?
Supplementary data links
Dataset links and DOIs 1 comment
Impact statements
links to  Figures
References 3 comments
links to Video files 
link to Letter to the author from board of reviewers and major comments (will have it's own DOI)
article abstract
link to Response from the author (will have it's own DOI)

﻿Given I have a DOI and a comment about one of the pieces of core article metadta, as a user of the API I want to PUT my comment on the article metadata


ALM Metdata

Given I have the DOI, as a user I want to be able to GET the article altmetrics that are available for the article.

Given I have a new metric for an article I want to be able to PUT that metadata onto the article.

Given I have an update to a metric for an article I want to be able to POST an update to that metadata onto the article.


Author Data

Author names
   Ordred by alpha | ordered by appearance
correspondence address
affiliation
contribution
ORCID



Composite Queries

Find: All articles written by a particular author
Find: All articles by institution / laboratory
Find: All articles by keyword(s)
Find: All articles by gene
Find: All articles by country (?)
Find: All articles by date of publication, or range of dates


-----

Article
Abstract only
Full text plus associated figures
Raw data (multiple sets per article)
Find: All articles written by a particular author
Find: All articles by institution / laboratory
Find: All articles by keyword(s)
Find: All articles by gene
Find: All articles by country (?)
Find: All articles by date of publication, or range of dates

Author
List of all author names, sorted alphabetically
Author full detail (ORCID, bio, photo)
Find: Author detail by name

Keywords
All keywords, each with frequency found -> tag cloud


