from django.conf.urls import patterns, url, include
from django.contrib import admin

from .view import PostsListView, PostDetailView
from .settings import settings


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', PostsListView.as_view()),
                       url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
                       url(r'^admin/', include(admin.site.urls)),)
