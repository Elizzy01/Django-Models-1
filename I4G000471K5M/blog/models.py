from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField((""))
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'blog_post')
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
