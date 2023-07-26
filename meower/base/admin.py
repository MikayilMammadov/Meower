from django.contrib import admin
from .models import Tweet, Comment, User

admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Comment)
