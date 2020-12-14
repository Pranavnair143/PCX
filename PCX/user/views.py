from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from user.forms import SignUpForm,UpdateProfileForm
from django.contrib.auth.models import User


from django.views.generic import TemplateView
from .models import UserProfile



@login_required(login_url='login/')
def user_profile(request):
    current_user=request.user
    profile=UserProfile.objects.get(user_id=current_user.id)
    context={'profile':profile}
    return render(request,'user_profile.html',context)

def login_form(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,'Login Failed..!!!Username or password incorrect.')
            return HttpResponseRedirect('/login')
    context={}
    return render(request,'log_in.html',context)

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup_form(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=request.POST['username']
            password=request.POST['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            current_user=request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.save()
            messages.success(request,'Your account has been created')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/')
    form=SignUpForm()
    context={'form':form}
    return render(request,'sign_up.html',context)

@login_required(login_url='login/')
def profile_update(request):
    if request.method=='POST':
        form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been updated!')
            return HttpResponseRedirect('/user/profile')
    else:
        profile_info=UserProfile.objects.filter(user_id=request.user.id)
        if profile_info:
            form=UpdateProfileForm(instance=request.user.userprofile)
        else:
            form=UpdateProfileForm()
        context={'form':form}
        return render(request,'user_update.html',context)