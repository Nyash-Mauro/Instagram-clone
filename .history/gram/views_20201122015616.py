from django import forms
from django.http import HttpResponse
from django.shortcuts import render,redirect
from cloudinary.forms import cl_init_js_callbacks      
from .models import Profile,Comments
from .forms import PhotoForm
from vote.managers import  VotableManager

votes = VotableManager()


def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'upload.html', context)
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all() 
    
    return render(request, 'socioapp/index.html',{"images":images})

def image_upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = ImageUploadForm()
        return render(request,'socioapp/upload.html', {"form":form})
