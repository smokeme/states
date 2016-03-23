#!/usr/bin/env python
import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'states.settings')
import django
from main.models import State, StateCapital, StateCities
django.setup()

# for state in states:
# 	print state.name

dir_path = os.path.dirname(os.path.abspath(__file__))
states_csv = os.path.join(dir_path, 'cities.csv')
csv_file = open(states_csv, 'r')

print csv_file

reader = csv.DictReader(csv_file)

from termcolor import colored
StateCities.objects.all().delete()
for row in reader:
	# print row['state']
	# print row['abbrev']
	# print row['capital']
	# print row['longitude']
	# print row['population']
	new_city, status = StateCities.objects.get_or_create(city=row['city'])
#	print "Status for %s is:" % new_city.city,
#	if (status == False):
#		print colored(status, 'red')
#	if (status == True):
#		print colored(status, 'yellow')
#	print row['state']
	if row['latitude']:
		new_city.latitude = row['latitude']
	if row ['longitude']: 
		new_city.longitude = row['longitude']
#	if row['county']:
	new_city.county = row['county']
#	if row['zip_code']:
	new_city.zip_code = row['zip_code']
	new_city.state , status= State.objects.get_or_create(abbreviation=row['state'])

	try:
		new_city.save()
	except Exception, e:
		print e
		print row