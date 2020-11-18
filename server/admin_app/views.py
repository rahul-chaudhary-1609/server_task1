from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserInfo
from django.contrib import messages

# Create your views here.

def signin(request):
    if request.method == 'POST':
        pass
    elif request.method=='GET':
        return render(request,'signin.html')
    

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['login_id']
        mobile = request.POST['mobile']
        password = request.POST['login_pass']
        
        if not UserInfo.objects.filter(email=email).exists():
            user=UserInfo(first_name=first_name, last_name=last_name, mobile=mobile, password=password, email=email)
            user.save()
            request.session['logged_user'] = email
            request.session.set_expiry(3000)
            messages.success(request, 'Registration Succesfull')
            return redirect('/profile')
        
        else:
            messages.error(request, 'User With Same Email Already Exists. Please use any other email')
            return redirect('/signup')


    elif request.method=='GET':
        return render(request, 'signup.html')
        

def profile(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request, 'profile.html', {"name": "Rahul Chaudhary", "email": "rahulchaudhary99r@gmail.com", "mobile": "9555269399", "ids": ["abc@gmail.com", "xyz@gmail.com"]})
        


def delete(request):
    pass

def logout(request):
    pass