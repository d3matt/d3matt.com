from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    edited = models.BooleanField()
    author = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    content = models.TextField()

# Create your models here.
