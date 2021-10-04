from django.contrib import admin
from superensino.quiz.models import Quiz, Question, Answer, MarksOfUser, Option


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(MarksOfUser)
admin.site.register(Answer)


