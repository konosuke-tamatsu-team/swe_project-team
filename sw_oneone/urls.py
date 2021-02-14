# coding: utf-8

from rest_framework import routers
from .views import UserViewSet, QuestionViewSet,WorkedQuestionViewSet,Logout

from django.conf.urls import include, url
from .views import AuthRegister

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^logout/', Logout.as_view()),
]

router = routers.DefaultRouter()
router.register('workedQuestios', WorkedQuestionViewSet)
router.register(r'users', UserViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'workedQuestios', WorkedQuestionViewSet)
url(r'^logout/', Logout.as_view()),
url(r'^register/$', AuthRegister.as_view()),
