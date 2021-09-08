from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import extendedUser
from  django.contrib import auth



def register(request):
    
    if request.method=='POST':
        if(request.POST['password1']==request.POST['password2']):
        
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'register.html',{'messages':'User exists with username'})
            
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                register=request.POST['register']
                
                newextendedUser=extendedUser(register=register,user=user)
                newextendedUser.save()
                auth.login(request,user)
                
                return redirect('home')

        else:
            return render(request,'register.html',{'messages':'Pass dont match'})
        
    return render(request,'users/register.html')


def login(request):
    
    if request.method=='POST':
        
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        
        if user is not None:
            auth.login(request,user)
            return HttpResponse('Success')
        else:
            return HttpResponse('Invalid')
            
    else:      
        return render(request,'users/login.html')


def chatbot(request):
    
    return render (request,'users/chatbot.html')