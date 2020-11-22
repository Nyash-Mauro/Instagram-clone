from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks
from .models import Profile, Comments
from .forms import PhotoForm
from vote.managers import VotableManager


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
