# coding: utf-8

from rest_framework import routers
from .views import UserViewSet, QuestionViewSet,Logout

from django.conf.urls import include, url
from .views import AuthRegister

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^logout/', Logout.as_view()),
]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'questions', QuestionViewSet)
url(r'^logout/', Logout.as_view()),
url(r'^register/$', AuthRegister.as_view()),
