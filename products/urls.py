from django.urls import path

#  #generic uchun
# from .views import ListCreateApi, DetailView
# #
# urlpatterns = [
#     path('', ListCreateApi.as_view()),
#     path('u/<int:pk>/', DetailView.as_view()),
# ]


#  #api view uchun
from .views import ChocolateListAPIView , ChocoDetailAPIView
urlpatterns = [
    path('' , ChocolateListAPIView.as_view()),
    path('u/<int:pk>/' , ChocoDetailAPIView.as_view())
]