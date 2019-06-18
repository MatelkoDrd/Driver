from django.urls import path
from .views import *

urlpatterns = [

    path('threads/', ThreadListView.as_view()),
    path('threads/<int:pk>', ThreadDetailView.as_view()),
]
