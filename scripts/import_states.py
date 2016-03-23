#!/usr/bin/env python
import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'states.settings')
import django
from main.models import State, StateCapital
django.setup()

# for state in states:
# 	print state.name

dir_path = os.path.dirname(os.path.abspath(__file__))
states_csv = os.path.join(dir_path, 'states.csv')
csv_file = open(states_csv, 'r')

print csv_file

reader = csv.DictReader(csv_file)

from termcolor import colored
State.objects.all().delete()
StateCapital.objects.all().delete()
for row in reader:
	# print row['state']
	# print row['abbrev']
	# print row['capital']
	# print row['longitude']
	# print row['population']
	new_state, status = State.objects.get_or_create(name=row['state'])
	print "Status for %s is:" % new_state.name,
	if (status == False):
		print colored(status, 'red')
	if (status == True):
		print colored(status, 'yellow')
	new_state.abbreviation = row['abbrev']
	new_state.save()

	new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])
	new_capital.state = new_state
	new_capital.latitude = row['latitude']
	new_capital.longitude = row['longitude']
	new_capital.population = row['population']
	new_capital.save()