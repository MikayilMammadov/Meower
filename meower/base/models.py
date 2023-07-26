from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Tweet(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=100)
    content = models.CharField(max_length=280, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="tweet_likes", default=None, blank=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ["-created"]

class Like(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tweet)

class Comment(models.Model):
    creator = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]




    
    

