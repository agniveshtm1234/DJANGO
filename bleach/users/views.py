from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
# User Authentication System
def user_login(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('list')
        else:
            error = "Invalid Credentials"
    return render(request,'users/login.html',{'error_msg':error})

def user_logout(request):
    logout(request)
    return redirect('home_page')

def signup(request):
    user = None
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username,password=password)
            redirect('user_login')
        except Exception as e:
            error=str(e)
    return render(request,'users/signup.html',{'user':user,'error_message':error})
