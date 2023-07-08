from django.db import models

# Create your models here.

class Tweet(models.Model):
    #creator =
    topic = models.CharField(max_length=100)
    content = models.TextField(max_length=280, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic
    

