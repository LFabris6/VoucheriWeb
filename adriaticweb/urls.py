
from django.contrib import admin
from django.urls import path
from web import views
from django.conf import settings
from django.views.static import serve
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('/static/finals/final.pdf>', views.download_file),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    re_path('', include('pwa.urls')),
]
