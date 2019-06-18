from rest_framework import serializers
from .models import Thread, Message


class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'title', 'description', 'user')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'description', 'user', 'message_thread')