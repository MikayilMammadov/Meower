from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tweet/<str:pk>/', views.tweet, name="tweet"),
    path('create-tweet/', views.create_tweet, name="create_tweet"),
    path("update-tweet/<str:pk>/", views.update_tweet, name="update_tweet"),
    path("delete-tweet/<str:pk>/", views.delete_tweet, name="delete_tweet"),
    path('login/', views.login_page, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    path('tweet/<int:tweet_id>/comment/', views.create_comment, name='create_comment'),
    path('like/<int:pk>/', views.like_tweet, name="like_tweet"),
    path('profile/', views.profile, name='profile'),

]