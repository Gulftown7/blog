from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
# MVC Model View Controller

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    
    def __str__(self):
        return self.title
