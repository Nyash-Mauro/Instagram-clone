from django.db import models
from django import forms
from cloudinary.models import CloudinaryField
from . models import Profile,Comments

class Photo(v,models.Model):
  image = CloudinaryField('image')

