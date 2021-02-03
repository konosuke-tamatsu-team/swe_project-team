# coding: utf-8

from rest_framework import routers
from .views import UserViewSet, QuestionViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'questions', QuestionViewSet)