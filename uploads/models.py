from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    public=models.BooleanField(default=False)
  

class Images(models.Model):
    post = models.ForeignKey(Post, default=None,on_delete=models.CASCADE)
    image = models.ImageField()
