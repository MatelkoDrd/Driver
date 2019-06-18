from django.contrib.auth.models import User
from django.db import models


class AdviceCategory(models.Model):
    name = models.CharField(max_length=64)


class Advice(models.Model):
    category = models.ForeignKey(AdviceCategory, on_delete=models.CASCADE)
    tags = models.CharField(max_length=32)
    description = models.TextField()


class AdviceQuestion(models.Model):
    question = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE)
