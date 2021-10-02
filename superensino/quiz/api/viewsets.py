from rest_framework.viewsets import ModelViewSet

from superensino.quiz.api.serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, MarksOfUserSerializer
from superensino.quiz.models import Quiz, Question, Answer, MarksOfUser


class QuizViewSet(ModelViewSet):
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.all()


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()


class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.all()


class MarksOfUserViewSet(ModelViewSet):
    serializer_class = MarksOfUserSerializer

    def get_queryset(self):
        return MarksOfUser.objects.all()