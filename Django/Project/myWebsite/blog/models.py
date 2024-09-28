from django.db import models
from django.urls import reverse # HP 10 L1
from django.contrib.auth.models import User # HP 10 L1

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    # HP 10 L1
    # ForeignKey to User model (author of the post)
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("model_detail", args=[str(self.id)])
    
