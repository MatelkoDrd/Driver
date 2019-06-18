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


# class AdviceListView(generics.ListCreateAPIView):
#     queryset = Advice.objects.all()
#     serializer_class = AdviceSerializer
#     ordering = ('id',)
#
#
# class AdviceDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Advice.objects.all()
#     serializer_class = AdviceSerializer



