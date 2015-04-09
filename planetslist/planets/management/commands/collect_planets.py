import os
import re
import requests
import json

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
	help = 'Escape css vars in site static directory http://dev.w3.org/csswg/css-variables/#defining-variables'

	def handle(self, *args, **options):
		planets = range(1, 61)
		for i in range(1, 61):
			obj = json.loads('{"pk": ' + str(i) + ',"model": "planets.planet","fields": ' + requests.get(
				'http://swapi.co/api/planets/' + str(i)).text + '}')
			obj['fields'].pop('residents')
			obj['fields'].pop('films')
			planets[i - 1] = obj

		with open("loaded_planets.json", "w") as outfile:
			json.dump(planets, outfile, indent=4)
