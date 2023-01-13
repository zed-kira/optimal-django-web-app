from django.shortcuts import render
from django.views.generic.base import TemplateView # new


class HomePageView(TemplateView): # new
    template_name = "home.html" # new