from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.blog_home, {'url_name':'blogs', 
                                 'get':views.get_blog_home,
                                 'post':views.post_blog_home}),
    url(r'^added/$', views.blog_added),
    ]