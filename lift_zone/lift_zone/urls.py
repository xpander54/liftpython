from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/$', include('grappelli.urls')), # URLS de django-grappelli
    url(r'^admin/', include(admin.site.urls)), # URLS del admin
    url(r'^', include('blog.urls')), # URLS del blog
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
