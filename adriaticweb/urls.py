
from django.contrib import admin
from django.urls import path
from web import views
from django.conf import settings
from django.views.static import serve
from django.urls import re_path as url
from django.urls import include

from rest_framework import routers
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

router = routers.DefaultRouter()
router.register('devices', FCMDeviceAuthorizedViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.apitest),
    path('test/', views.test),
    path('api/', include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    url('', include('pwa.urls')),
    path('firebase-messaging-sw.js', views.ServiceWorkerView.as_view(), name='service_worker'),
]
