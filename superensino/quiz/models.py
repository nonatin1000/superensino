from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    number_of_questions = models.IntegerField(default=4)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Exercício'
        verbose_name_plural = 'Exercícios'

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.questions.all()


class Question(models.Model):
    content = models.TextField()
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'

    def __str__(self):
        return self.content


class Option(models.Model):
    content = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'

    def __str__(self):
        return f"question: {self.question.pk}, answer: {self.content}, correct: {self.is_correct}"


class MarksOfUser(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Teste'
        verbose_name_plural = 'Testes'

    @property
    def accepts(self):
        return Answer.objects.filter(marks_of_user=self, option__is_correct=True).count()

    @property
    def faults(self):
        return Answer.objects.filter(marks_of_user=self).exclude(option__is_correct=True).count()

    @property
    def score(self):
        accepts = self.accepts
        questions = self.quiz.number_of_questions
        return round(accepts/questions*100,2)

    def __str__(self):
        return str(self.quiz)


class Answer(models.Model):
    marks_of_user = models.ForeignKey(MarksOfUser, related_name='answers', on_delete=models.CASCADE)

    option = models.ForeignKey(Option, related_name='answers', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

    def __str__(self):
        return f"question: {self.option.question.pk}, answer: {self.option.pk} - {self.option.content}, correct: {self.option.is_correct}"
