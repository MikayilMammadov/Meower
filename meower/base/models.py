from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    creator = models.ForeignKey(User,  on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=100)
    content = models.TextField(max_length=280, null=True, blank=True)
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
        return str(self.post)


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[0:50]




    
    

