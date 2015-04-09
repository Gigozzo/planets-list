from django.db import models


class Planet(models.Model):
	name = models.CharField(max_length=255)
	rotation_period = models.CharField(max_length=255)
	orbital_period = models.CharField(max_length=255)
	diameter = models.CharField(max_length=255)
	climate = models.CharField(max_length=255)
	gravity = models.CharField(max_length=255)
	terrain = models.CharField(max_length=255)
	surface_water = models.CharField(max_length=255)
	population = models.CharField(max_length=255)
	created = models.DateTimeField(editable=False)
	edited = models.DateTimeField()
	url = models.CharField(max_length=255)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/planets/%i/" % self.id