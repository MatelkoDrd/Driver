from rest_framework import generics
from .models import Answer, Question, Quiz
from .serializers import AnswerSerializer, QuestionSerializer, QuizSerializer


class QuizListView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    ordering = ('id',)


class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


