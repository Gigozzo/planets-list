from django.db import models

class Planet(models.Model):
    title = models.CharField(max_length=255)
    diameter = models.CharField(max_length=255)
    surfacewater = models.CharField(max_length=255)
    population = models.CharField(max_length=255)
    gravity = models.CharField(max_length=255)
    climate = models.CharField(max_length=255)
    orbitalperiod = models.CharField(max_length=255)
    terrain = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/planets/%i/" % self.id