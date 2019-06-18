from django.db import models
from advices.models import Advice


class Quiz(models.Model):
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE)


class Question(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class Answer(models.Model):
    description = models.CharField(max_length=128)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
