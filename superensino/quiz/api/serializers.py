from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from superensino.quiz.models import Quiz, Question, Answer, MarksOfUser


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    quiz = QuizSerializer()

    class Meta:
        model = Question
        fields = ('content', 'quiz',)


class AnswerSerializer(ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = '__all__'


class MarksOfUserSerializer(ModelSerializer):
    quiz = QuizSerializer()

    class Meta:
        model = MarksOfUser
        fields = '__all__'
