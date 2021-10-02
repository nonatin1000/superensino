from django.urls import path, include
from superensino.quiz import api

app_name = 'quiz'

urlpatterns = [
    path('api/', include('superensino.quiz.api.urls')),
]
