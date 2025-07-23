from django.urls import path
from .views import analytics , chat


urlpatterns = [
    path('analysis' , analytics) ,
    path('ask' , chat)
]