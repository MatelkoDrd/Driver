from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Thread(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
