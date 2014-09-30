from django.conf.urls import patterns, include, url
# from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name = 'index'),
)
