from django.db import models
from django import forms
from cloudinary.models import CloudinaryField
from . models import Profile,Comments

class Photo(VoteModel,models.Model):
  image = CloudinaryField('image')

