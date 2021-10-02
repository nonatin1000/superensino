from django.contrib import admin
from superensino.quiz.models import Quiz, Question, Answer, MarksOfUser


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(MarksOfUser)

