from django.conf.urls import url
from . import views


app_name = 'projects'

urlpatterns = [
    url(r'^$', views.ProjectIndexView.as_view(), name='index')
]