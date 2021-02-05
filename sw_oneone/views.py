import django_filters
from rest_framework import viewsets, filters
from django.http import HttpResponse
from rest_framework.response import Response

from .models import User, Question
from .serializer import UserSerializer, QuestionSerializer
import json
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

   

    