from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tweet/<str:pk>/', views.tweet, name="tweet"),

]