from django.urls import path
from .views import *

urlpatterns = [
    path('' , ListCreateApi.as_view()),
    path('u/<int:pk>/' , DetailView.as_view()),
]