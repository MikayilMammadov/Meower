from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tweet/<str:pk>/', views.tweet, name="tweet"),
    path('create-tweet/', views.create_tweet, name="create_tweet"),
    path('login/', views.login_page, name="login"),

]