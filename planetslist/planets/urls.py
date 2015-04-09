#coding: utf-8
from django.conf.urls import patterns, url

from planets.views import PlanetsListView, PlanetDetailView

urlpatterns = patterns('',
	url(r'^$', PlanetsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/
)