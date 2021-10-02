from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    number_of_questions = models.IntegerField(default=4)

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.questions.all()


class Question(models.Model):
    content = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_answers(self):
        return self.answers.all()


class Answer(models.Model):
    content = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.content}, answer: {self.content}, correct: {self.correct}"


class MarksOfUser(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.quiz)