
from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from users.models import extendedUser
import pickle 
import joblib
import pathlib
from django.contrib.auth.decorators import login_required




@login_required(login_url='/users/login/')
def home(request):
    current_user=request.user
    curr_ext=extendedUser.objects.get(user=current_user)
    registered=curr_ext.register
    
    if(registered=='NGO'):
        register_as='1'
    else:
        register_as='0'
    
    print(register_as)
    
    return render(request,'main/home.html',{'register_as':register_as})

def about(request):
    return render(request,'main/about_us.html')

def contact(request):
    return render(request,'main/contact_us.html')


def tracker(request):
    return render (request,'main/tracker.html')

#---#

import sys
sys.path.insert(0, 'D:/xhacks/xhacks/Model')

from model import model_1

def getPrediction(st,age,gender,inp_cause):
    
    filename='model.sav'
    abspath = pathlib.Path(filename).absolute()
    
    
    
    model = pickle.load(open(abspath,'rb'))
    result=model(st,age,gender,inp_cause)
    
    return result


    
    
def NGO(request):
    return render(request,'main/NGO/NGO.html')

def funding(request):
    return render(request,'main/NGO/funding.html')
    
def suicide(request):
    return render(request,'main/NGO/suicide.html')

def contribute(request):
    return render(request,'main/NGO/contribute.html')

def survey(request):
    return render(request,'main/survey.html') 

def result(request):
    
    
    region=request.POST.get('region')
    age=int(request.POST.get('age'))
    gender=request.POST.get('gender')
    cause=request.POST.get('cause')
    
    if(age>14 and age<60 ):
        x=round(age/14)
        
        low=(14*x+x)
        high=low+14
        
    elif(age<14):
        low=0
        high=14
    else:
        low=60
        high='above'
        
    
    
    ans=getPrediction(region,age,gender,cause)
    
    
    return render (request,'main/NGO/result.html',{'result':ans,'region':region,'cause':cause,'low':low,'high':high})