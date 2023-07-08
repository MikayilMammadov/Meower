from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tweet

# Create your views here.

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
