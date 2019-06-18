from django.urls import path
from .views import *


urlpatterns = [

    path('quizes/', QuizListView.as_view()),
    path('quizes/<int:pk>', QuizDetailView.as_view()),

]