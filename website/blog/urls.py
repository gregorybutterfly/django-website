from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.PostView.as_view(), name='post'),
]