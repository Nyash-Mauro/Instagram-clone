from django.forms import ModelForm      
from .models import Photo

class PhotoForm(ModelForm):
  class Meta:
      model = Photo
from . models import Image,Profile,Comments

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','likes','comments','user']
        
class ImageProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','image','date_posted']
    
        