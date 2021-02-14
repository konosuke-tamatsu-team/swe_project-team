# coding: utf-8

from rest_framework import serializers

from .models import User, Question,WorkedQuestion


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ('id','name','password')
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        return User.objects.create_user(request_data=validated_data)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id','question', 'aChoice', 'dChoice1', 'dChoice2', 'dChoice3', 'dChoice4', 'comment', 'created_at', 'updated_at', 'author','is_past_question','number_of_times','field')

class WorkedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkedQuestion
        fields = ('id','uId','workedQuestion')