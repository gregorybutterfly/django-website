from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView

from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    #print('aaaaa',models.Category.objects.get(id=2).post_set.all())

    def posts(self):
        """ Return list of all posts """
        return models.Post.objects.all()

    def categories(self):
        """ Return list of all categories """
        return models.Category.objects.all()

    def tags(self):
        """ Return list of all tags """
        return models.Tag.objects.all()

class PostView(DetailView):
    model = models.Post

    pk_url_kwarg = 'pk'
    #slug_url_kwarg = 'slug'
    #query_pk_and_slug = True
    template_name = 'post.html'




