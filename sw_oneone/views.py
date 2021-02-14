import django_filters
from rest_framework import viewsets, filters, generics, permissions
from django.http import HttpResponse
from rest_framework.response import Response

from .models import User, Question,WorkedQuestion
from .serializer import UserSerializer, QuestionSerializer,WorkedQuestionSerializer
import json
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action
from rest_framework.views import APIView
import urllib.request

class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    print(2)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):


    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class WorkedQuestionViewSet(viewsets.ModelViewSet):
    print("検証")
    queryset = WorkedQuestion.objects.all()
    serializer_class = WorkedQuestion

class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



   

    