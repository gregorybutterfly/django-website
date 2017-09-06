from django.db import models
from django.utils import timezone


class Author(models.Model):
    """ Define info about the blog author """

    name = models.CharField('Authors name', max_length=30)
    bio = models.TextField('About Author')


class Category(models.Model):
    """ Define blog Categories """
    name = models.CharField('Category Name', max_length=30)


class Dates(models.Model):
    """ Define blog dates for posts and articles """
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(default=timezone.now)


class Tag(models.Model):
    name = models.CharField(max_length=10)


class Post(models.Model):
    """ Define blog post """
    title = models.CharField('Post title', max_length=200)
    body = models.TextField('Post Contents')
    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author)
    date = models.ForeignKey(Dates)
    tag = models.ForeignKey(Tag)