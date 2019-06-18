from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('categories/', AdviceCategoryListView.as_view()),
    path('categories/<int:pk>', AdviceCategoryDetailView.as_view()),

]

