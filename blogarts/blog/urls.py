from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.blog_home, {'url_name' : 'blogs'}),
    url(r'^added/$', views.blog_added),
    ]