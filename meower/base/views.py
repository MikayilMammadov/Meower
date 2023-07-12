from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Tweet, Comment
from .forms import TweetForm, CommentForm

# Create your views here.

def login_page(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exit")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password dose not exist")

    context = {"page":page}
    return render(request, "base/login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect("home")

def registerUser(request):
    page = "register"
    form = UserCreationForm()
    context = {"page":page, "form":form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Error occured during registration")


    return render(request, "base/login_register.html",context)

def home(request):
    tweets = Tweet.objects.all()
    #test
    comments = Comment.objects.all
    context = {"tweets":tweets, "comments":comments}
    return render(request, "base/home.html", context)

def tweet(request, pk):
    tweet = None
    tweets = Tweet.objects.all()
    for i in tweets:
        if i['id']==int(pk):
            tweet = i
    context={"tweet":tweet}
    return HttpResponse("Tweet")

@login_required(login_url="/login")
def create_tweet(request):
    form = TweetForm()
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.creator = request.user  # Set the creator as the logged-in user
            tweet.save()
            return redirect('home')
    context = {"form": form}
    return render(request, 'base/create_tweet.html', context)

@login_required(login_url="/login")
def create_comment(request, tweet_id):
    tweet = Tweet.objects.get(pk=tweet_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.creator = request.user  # Set the creator as the logged-in user
            comment.tweet = tweet
            comment.save()
    else:
        form = CommentForm()

    return redirect('home')