warpandweft
===========

Warp and Weft is a linked open data, digital humanities project that is collecting record information on textiles from siloed collections and turning this information into RDF triples. 

Please visit the project at: http://dev-warp-and-weft.gotpantheon.com/

===========

<b>Cooper Hewitt Museum</b>

To collect data from the Cooper Hewitt we created a Python script to automate an API Get Request. 
Read an extended annoation of the code here: http://bit.ly/19kuCyd

<b>Metropolitan Museum</b>

The Metropolitan Museum does not currently have an API. In order to collect tombstone informaton about American textiles in their collection we created two Python scripts. The <a href="https://github.com/carolynlimadeo/warpandweft/blob/master/Met%20Screen%20Scrape%20Scripts/metscrape2.py">first script</a> iterated through all of the collection result pages and gathered all of the individual URLs for each object record. The <a href="https://github.com/carolynlimadeo/warpandweft/blob/master/Met%20Screen%20Scrape%20Scripts/metscrape2.py"> used the Python library <a href="http://www.crummy.com/software/BeautifulSoup/"> Beautiful Soup</a> to scrape the tombstone information from each record and format it as a .json file. 

Check back soon for an extended annotation of these two scripts.

