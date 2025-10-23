from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
# Create your views here.
# User Authentication System
@never_cache
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
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        has_error = False
        if password!=confirm_password:
            messages.error(request,"Passwords do not match. Please try again.")
            has_error=True
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists. Please choose another')
            has_error=True
        if has_error:
            return render(request,'users/signup.html')
        User.objects.create_user(username=username,password=password,email=email)
        messages.success(request,"You have Successfully Registered!! Please Log In")
        return redirect('user_login')
        
    return render(request,'users/signup.html')


"""Only use user.save() if you change the user object after it has been created 
   for eg:  user = User.objects.create_user(username = username,email=email)
            user.password = 'abcd'
            user.save()  --> here it is a must thing cuz user object got updated by adding password, you must 
                             save it
"""