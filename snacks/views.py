# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name='home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class SnacksView(TemplateView):
    template_name = 'snacks.html'
    
# Create your views here.
