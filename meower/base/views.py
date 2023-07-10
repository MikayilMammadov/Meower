from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm

# Create your views here.

def login_page(request):
    context = {}
    return render(request, "base/login_register.html", context)


def home(request):
    tweets = Tweet.objects.all()
    context = {"tweets":tweets}
    return render(request, "base/home.html", context)

def tweet(request, pk):
    tweet = None
    for i in tweets:
        if i['id']==int(pk):
            tweet = i
    context={"tweet":tweet}
    return HttpResponse("Tweet")

def create_tweet(request):
    form = TweetForm()
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={"form":form}
    return render(request, 'base/create_tweet.html', context)
