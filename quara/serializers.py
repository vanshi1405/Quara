from rest_framework import serializers

from quara.models import *

class AnswerSerializer(serializers.ModelSerializer):
    question_title = serializers.CharField(source='ques.title',read_only=True)
    no_of_likes = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ('updated_date',)

    def no_of_likes(self,instance):
        return len(instance.likes.all())

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('updated_date',)



