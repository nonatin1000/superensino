from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from superensino.quiz.api.serializers import QuizSerializer, AnswerSerializer
from superensino.quiz.models import Quiz, Answer, MarksOfUser, Option


class QuizViewSet(ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.filter(status=True)

    @action(methods=['post'], detail=True)
    def create_answer(self, request, pk):
        marks_of_user = MarksOfUser.objects.get(quiz_id=pk, user=self.request.user)
        option = Option.objects.get(pk=request.data['id_option'])
        Answer.objects.create(marks_of_user=marks_of_user, option=option)
        return HttpResponse('Resposta Salvas', status.HTTP_200_OK)


class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
