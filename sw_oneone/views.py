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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def retrieve(self, request, *args, **kwargs):
        return Response({'something': 'my custom JSON'})

    """def list(self, request, *args, **kwargs):
        queryset = Question.objects.all()
        serializer_class = QuestionSerializer
        print(queryset)
        mylist = []
        for question  in queryset:
            data={
                'id': question.id,
                'question': question.question,
                'aChoice': question.aChoice,
                'dChoice1': question.dChoice1,
                'dChoice2': question.dChoice2,
                'dChoice3': question.dChoice3,
                'dChoice4': question.dChoice4,
                'comment': question.comment,
                'author': question.author,
                },
            print(data)
            mylist.append(data)
       
        
       
        res_data = JSONRenderer().render(self.serializer_class(queryset, many=True).data)
        print(res_data)
        return Response(res_data)"""