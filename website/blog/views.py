from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def posts(self):
        return models.Post.objects.all()