from django import forms
from . models import Profile,Comments
from django.forms import ModelForm      
from .models import PhotoForm


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ['profile','likes','comments','user']
        
class ImageProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','image','date_posted']
    
        