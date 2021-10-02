from django.urls import path
from rest_framework import routers
from . import viewsets

app_name = "api"

router = routers.SimpleRouter()
router.register(r'quiz', viewsets.QuizViewSet, basename="quiz")
router.register(r'question', viewsets.QuestionViewSet, basename="quiz")
router.register(r'answer', viewsets.AnswerViewSet, basename="quiz")
router.register(r'marks-of-user', viewsets.MarksOfUserViewSet, basename="quiz")

urlpatterns = [

]

urlpatterns += router.urls
