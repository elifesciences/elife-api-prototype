import sys
import getopt
import settings
import json
import parseFI as fim

def load_fake_alm():
	"""
	Load some fake ALM data into Fluidinfo for demonstration purposes
	"""

	# Fake ALM source
	fake_alm_source = [
		{
			'about': 'elife_alm_source_fake',
			'source': 'fake',
			'url': 'http://www.elifesciences.org/',
			'name': 'fake',
			'trusted': False,
		}
	]
	
	for data in fake_alm_source:
		about = data['about']
		obj = fim.fi_alm_source();
		obj.create(about = about);
		
		obj.source = data['source']
		obj.url = data['url']
		obj.name = data['name']
		obj.trusted = data['trusted']
		
		obj.save()
		
		print "ALM source UID: " + obj.uid

	# Fake ALM data
	fake_alm = [
		{
			'about': 'elife_alm_fake_web_day_October_15_2012_10.7554/eLife.00013',
			'doi': '10.7554/eLife.00013',
			'alm_source': 'fake',
			'type': 'web',
			'value': 8,
			'timespan': 'day',
			'date_date': 'October 15, 2012',
			'date_day': 15,
			'date_month': 10,
			'date_year': 2012,
			'date_timestamp': 1350259200,
			'complete': True,
		},
		{
			'about': 'elife_alm_fake_web_day_October_16_2012_10.7554/eLife.00013',
			'doi': '10.7554/eLife.00013',
			'alm_source': 'fake',
			'type': 'web',
			'value': 13,
			'timespan': 'day',
			'date_date': 'October 16, 2012',
			'date_day': 16,
			'date_month': 10,
			'date_year': 2012,
			'date_timestamp': 1350345600,
			'complete': True,
		},
		{
			'about': 'elife_alm_fake_web_day_October_17_2012_10.7554/eLife.00013',
			'doi': '10.7554/eLife.00013',
			'alm_source': 'fake',
			'type': 'web',
			'value': 18,
			'timespan': 'day',
			'date_date': 'October 17, 2012',
			'date_day': 17,
			'date_month': 10,
			'date_year': 2012,
			'date_timestamp': 1350432000,
			'complete': True,
		},
		{
			'about': 'elife_alm_fake_web_day_October_18_2012_10.7554/eLife.00013',
			'doi': '10.7554/eLife.00013',
			'alm_source': 'fake',
			'type': 'web',
			'value': 43,
			'timespan': 'day',
			'date_date': 'October 18, 2012',
			'date_day': 18,
			'date_month': 10,
			'date_year': 2012,
			'date_timestamp': 1350518400,
			'complete': True,
		},
		{
			'about': 'elife_alm_fake_web_day_October_19_2012_10.7554/eLife.00013',
			'doi': '10.7554/eLife.00013',
			'alm_source': 'fake',
			'type': 'web',
			'value': 48,
			'timespan': 'day',
			'date_date': 'October 19, 2012',
			'date_day': 19,
			'date_month': 10,
			'date_year': 2012,
			'date_timestamp': 1350604800,
			'complete': True,
		},
		{
			'about': 'elife_alm_fake_web_day_October_20_2012_10.7554/eLife.00013',
			'doi': '10.7554/eLife.00013',
			'alm_source': 'fake',
			'type': 'web',
			'value': 52,
			'timespan': 'day',
			'date_date': 'October 20, 2012',
			'date_day': 20,
			'date_month': 10,
			'date_year': 2012,
			'date_timestamp': 1350691200,
			'complete': True,
		},
		{
			'about': 'elife_alm_fake_web_day_October_21_2012_10.7554/eLife.00013',
			'doi': '10.7554/eLife.00013',
			'alm_source': 'fake',
			'type': 'web',
			'value': 36,
			'timespan': 'day',
			'date_date': 'October 21, 2012',
			'date_day': 21,
			'date_month': 10,
			'date_year': 2012,
			'date_timestamp': 1350777600,
			'complete': True,
		},
		
	]
	
	for data in fake_alm:
		about = data['about']
		obj = fim.fi_alm();
		obj.create(about = about);
		
		obj.alm_source = data['alm_source']
		obj.doi = data['doi']
		obj.type = data['type']
		obj.value = data['value']
		obj.timespan = data['timespan']
		obj.date_date = data['date_date']
		obj.date_day = data['date_day']
		obj.date_month = data['date_month']
		obj.date_year = data['date_year']
		obj.date_timestamp = data['date_timestamp']
		obj.complete = data['complete']
		
		obj.save()
		
		print "ALM UID: " + obj.uid
	
def main(argv=None):
	load_fake_alm()
	
if __name__ == "__main__":
	main()