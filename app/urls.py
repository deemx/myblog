from django.conf.urls import patterns, url, include
from django.contrib import admin

from .view import PostsListView, PostDetailView


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', PostsListView.as_view()),
                       url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^captcha/', include('captcha.urls')),)
