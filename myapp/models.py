# Create your models here.
from django.db import models
from django.utils import timezone




class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Blog (models.Model):
   title = models.CharField(max_length=100)
   date = models.DateTimeField(default=timezone.now)
   img = models.ImageField(upload_to='media/')
   contents = models.TextField(max_length=100)
   is_tea = models.BooleanField(default=False)
   #追加
   def __str__(self):
       return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Login(models.Model):
    pscord = models.CharField(max_length=8)
