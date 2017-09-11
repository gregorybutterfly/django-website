from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class MyHomeView(TemplateView):
    template_name = 'home.html'

