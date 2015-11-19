"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from polls.views import main_page, get_post, posts_page, auth, we , blog, profile, get_blog_post
from django.conf.urls import patterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
               (r'^post/([0-9]{1,5})', get_post),
                (r'^$', main_page),
                       (r'^posts/', posts_page),
                            (r'^auth/', auth),
                                (r'^we/', we),
                       (r'^blog/', blog),
                       (r'^profile/', profile),
                       (r'^blog_post/([0-9]{1,5})', get_blog_post),
                       
               
)