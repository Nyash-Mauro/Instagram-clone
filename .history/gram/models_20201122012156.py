from django.db import models
from django import forms
from cloudinary.models import CloudinaryField
from . models import Profile,Comments
from tinymce.models import HTMLField
from vote.models import VoteModel
from django.contrib.auth.models import User

class Photo(VoteModel,models.Model):
  image = CloudinaryField('image')
  image_name = models.CharField(max_length=50)
  image_caption = models.CharField(max_length=100)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
