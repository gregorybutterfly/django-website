from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.PostView.as_view(), name='post'),
    url(r'^login$', login, {'template_name':'login.html'}),
    url(r'^profile$', views.ProfileView.as_view())
]