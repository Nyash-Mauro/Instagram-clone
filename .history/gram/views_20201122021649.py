from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks
from .models import Profile, Comments
from .forms import PhotoForm,ImageProfileForm,CommentForm
from vote.managers import VotableManager
from .models import *

votes = VotableManager()


@login_required(login_url='/accounts/login/')
def home(request):
    images = PhotoForm.objects.all()

    return render(request, 'socioapp/index.html', {"images": images})


def upload(request):
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'upload.html', context)


def profile_info(request):

    current_user = request.user
    profile_info = Profile.objects.filter(user=current_user).first()
    posts = request.user.image_set.all()

    return render(request, 'grammies/profile.html', {"images": posts, "profile": profile_info, "current_user": current_user})


def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = PhotoForm()
        return render(request, 'gramies/edit.html', {"form": form})
def add_comment(request,id):

    current_user = request.user
    image = PhotoForm.get_single_photo(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image_id = id
            comment.save()
        return redirect('home')

    else:
        form = CommentForm()
        return render(request,'grammies/new_comment.html',{"form":form,"image":image})
def comments(request,id):
    comments = Comments.get_comments(id)
    number = len(comments   )
    
    return render(request,'grammies/comments.html',{"comments":comments,"number":number})        

@login_required (login_url='/accounts/register/')
def like_images(request,id):
    image =  PhotoForm.get_single_photo(id)
    user = request.user
    user_id = user.id
    
    if user.is_authenticated:
        uplike = image.votes.up(user_id)
        image.likes = image.votes.count()
        image.save()
        
    return redirect('home')