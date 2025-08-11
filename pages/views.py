from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'base.html'

class AboutView(TemplateView):
    template_name = 'pages/aboutus.html'


