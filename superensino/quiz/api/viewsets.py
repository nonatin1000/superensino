from rest_framework.viewsets import ModelViewSet

from superensino.quiz.api.serializers import QuizSerializer, AnswerSerializer
from superensino.quiz.models import Quiz, Answer


class QuizViewSet(ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.filter(status=True)


class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
