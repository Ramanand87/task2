from . import models
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
def login(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['password']
        try:
            check=authenticate(username=User.objects.get(email=username),password=password)
        except:
            check=authenticate(username=username,password=password)
        if check is not None:
            auth.login(request,check)
            return redirect('profile')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
        
    return render(request,'login.html')
 
def register(request):
    if request.method=='POST':
        user_type=request.POST['user']
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        address=request.POST['address']
        pas=request.POST['passw']
        cnfpas=request.POST['cnfpassword']
        # image=request.POST['image']
        if models.User.objects.filter(email=email).exists():
            messages.info(request,'email already registered')
            return redirect('register')
        elif models.User.objects.filter(username=username).exists():
            messages.info(request,'Username already exists')
            return redirect('register')
        elif pas!=cnfpas:
            messages.info(request,"Password and Confirm password didn't match")
            return redirect('register')
        else:
            new_user=models.User.objects.create(username=username,email=email)
            new_user.set_password(pas)  
            new_user.save()
            new_prof=models.Profile.objects.create(user=new_user,name=name,address=address,user_type=user_type)
            new_prof.save()
            auth.login(request,new_user)
        return redirect('profile')
    return render(request,'register.html')
            
def profile(request):
    prof=models.Profile.objects.get(user=request.user)
    return render(request,'profile.html',{'prof':prof})