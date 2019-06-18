from rest_framework import generics
from .models import Thread, Message
from .serializers import MessageSerializer, ThreadSerializer


class ThreadListView(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    ordering = ('id',)


class ThreadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
