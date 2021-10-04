from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from superensino.quiz.models import Quiz, Question, Answer, MarksOfUser, Option


class QuizSerializer(ModelSerializer):
    started = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField()

    def get_started(self, obj):
        user = self.context["request"].user
        return obj.marksofuser_set.filter(user=user).exists()

    def get_questions(self, obj):
        return QuestionSerializer(obj.questions.all(), many=True, context=self.context).data

    def get_result(self, obj):
        try:
            mark_of_user = MarksOfUser.objects.get(
                user=self.context["request"].user,
                quiz=obj
            )
            return {
                "accepts": mark_of_user.accepts,
                "faults": mark_of_user.faults,
                "score": mark_of_user.score
            }
        except MarksOfUser.DoesNotExist:
            return None

    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    options = serializers.SerializerMethodField()

    def get_options(self, obj):
        return OptionSerializer(obj.options.all(), many=True, context=self.context).data

    class Meta:
        model = Question
        fields = ('content', "options")


class OptionSerializer(ModelSerializer):
    answered = serializers.SerializerMethodField()

    def get_answered(self, obj):
        try:
            mark_of_user = MarksOfUser.objects.get(
                user=self.context["request"].user,
                quiz=obj.question.quiz
            )
            return Answer.objects.filter(option=obj, marks_of_user=mark_of_user).exists()
        except MarksOfUser.DoesNotExist:
            return False

    class Meta:
        model = Option
        exclude = ["is_correct", "question"]


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

"""
    AnswerSerializer
        -> idOption
        Method:
            authenticated user
            Acoording of idOption to get quiz
            to get object mark of user
            to create Answer (mark of user, idOption)
"""