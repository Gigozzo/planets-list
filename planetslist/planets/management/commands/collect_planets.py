import os
import re
import requests
import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
	help = 'Escape css vars in site static directory http://dev.w3.org/csswg/css-variables/#defining-variables'

	def handle(self, *args, **options):
		planets = range(1,61)
		for i in range(1,61):
			obj = json.loads('{"pk": '+ str(i) +',"model": "planets.planet","fields": ' + requests.get('http://swapi.co/api/planets/' + str(i)).text + '}')
			obj['fields'].pop('residents')
			obj['fields'].pop('films')
			planets[i-1] = obj

		# planets-json = json.dumps(planets)

		# self.stdout.write(json.dumps(planets), ending='')
		# self.stdout.write(json.dumps(planets[1]['fields']), ending='')
		# self.stdout.write(json.dumps(planets[1]['fields']['residents']), ending='')
		# planets[1]['fields'].pop('residents')
		# planets[1]['fields'].pop('films')
		# self.stdout.write(json.dumps(planets[1]), ending='')

		with open("loaded_planets.json", "w") as outfile:
			json.dump(planets, outfile, indent=4)

		self.stdout.write("<<<2222<<< line", ending='')
		print 'Replaced >>>> variables'