# coding: utf-8

from django.conf.urls import url, include
from django.contrib import admin

from sw_oneone.urls import router as sw_oneone_router
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path

urlpatterns = [
    path('api/v1/rest-auth/', include('rest_auth.urls')), 
    path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
    url(r'^admin/', admin.site.urls),
    # blog.urlsをincludeする
    url(r'^api/', include(sw_oneone_router.urls)),
    path('auth/', obtain_jwt_token),
    
]