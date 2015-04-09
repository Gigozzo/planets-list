from django.shortcuts import render
from django.db import models
from planets.models import Planet
from django.views.generic import ListView, DetailView


class PlanetsListView(ListView):
	model = Planet