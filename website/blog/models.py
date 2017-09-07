from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode


class Author(models.Model):
    """ Define info about the blog author """

    name = models.CharField('Authors name', max_length=30)
    bio = models.TextField('About Author')

    def __str__(self):
        return self.name


class Category(models.Model):
    """ Define blog Categories """
    name = models.CharField('Category Name', max_length=30)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Dates(models.Model):
    """ Define blog dates for posts and articles """
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.updated)


class Tag(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))

        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    """ Define blog post """
    title = models.CharField('Post title', max_length=200)
    body = models.TextField('Post Contents')
    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author)
    date = models.ForeignKey(Dates)
    tag = models.ForeignKey(Tag)
    slug = models.SlugField(unique=True, blank=True)
    img = models.CharField(max_length=1000, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title