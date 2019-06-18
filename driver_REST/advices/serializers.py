from rest_framework import serializers
from .models import AdviceCategory, Advice, AdviceQuestion


class AdviceCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdviceCategory
        fields = ('id', 'name',)


class AdviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advice
        fields = ('id', 'category', 'tags', 'description',)


class AdviceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdviceQuestion
        fields = ('id', 'question', 'user', 'advice',)