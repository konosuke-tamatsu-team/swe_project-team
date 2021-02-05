# coding: utf-8

from rest_framework import serializers

from .models import User, Question


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id','question', 'aChoice', 'dChoice1', 'dChoice2', 'dChoice3', 'dChoice4', 'comment', 'created_at', 'updated_at', 'author')