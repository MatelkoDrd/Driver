from rest_framework import generics
from .models import Advice, AdviceQuestion, AdviceCategory
from .serializers import AdviceCategorySerializer, AdviceQuestionSerializer, AdviceSerializer
# Create your views here.


class AdviceCategoryListView(generics.ListCreateAPIView):
    queryset = AdviceCategory.objects.all()
    serializer_class = AdviceCategorySerializer
    ordering = ('id',)


class AdviceCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdviceCategory.objects.all()
    serializer_class = AdviceCategorySerializer




