from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import *
# Create your views here.



def index(request):
    return render(request,'index.html')



def blog(request):
    post=Blog.objects.all()
    context={'posts':post}
    return render(request,'blog.html',context)

def query1(request):
    if request.method =='POST': 
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphone=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=contact(name=fname,email=femail,phonenumber=fphone,desc=fdesc)
        query.save()
        messages.success(request,'Thanks for contacting us. we will get you soon! ')
        return redirect(query1)
    return render(request,'contact.html')