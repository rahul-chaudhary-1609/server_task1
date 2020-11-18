from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserInfo
from django.contrib import messages

# Create your views here.

def signin(request):
    if request.method == 'POST':
        email = request.POST['login_id']
        password = request.POST['login_pass']
        if UserInfo.objects.filter(email=email,password=password).exists():
            request.session['logged_user'] = email
            #request.session.set_expiry(3000)
            return redirect('/profile')        
        else:
            return redirect('/signup')

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
            #request.session.set_expiry(3000)
            messages.success(request, 'Registration Succesfull')
            return redirect('/profile')
        
        else:
            messages.error(request, 'User With Same Email Already Exists. Please use any other email')
            return redirect('/signup')


    elif request.method=='GET':
        return render(request, 'signup.html')
        

def profile(request):
    if 'logged_user' in request.session:
        logged_user = request.session['logged_user']
        profile_user = UserInfo.objects.get(email=logged_user)
        users = UserInfo.objects.all()
        print(users)
        return render(request, 'profile.html', {"name": profile_user.first_name, "email": profile_user.email, "mobile": profile_user.mobile, "ids": [e.email for e in users]})
    


def delete(request):
    if request.method == 'POST':
        email = request.POST['login_ids']
        user = UserInfo.objects.get(email=email)
        user.delete()
        logged_user = request.session['logged_user']
        if email == logged_user:
            request.session.pop('logged_user',None)
            return redirect('/signin')
        else:
            return redirect('/profile')

def logout(request):
    pass