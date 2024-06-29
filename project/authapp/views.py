from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('signup')  
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                user=authenticate(username=username,password=password1)
                if user is not None:
                    auth.login(request,user)
                    messages.success(request,"Login Successful")
                    return redirect('/')                
        else:
            messages.info(request,"Password not match")
            return redirect('signup')
    else:
        return render(request,'signup.html')
    

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,'invalide password')
            return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    messages.success(request,"Logout Successful")
    return redirect('/')
 