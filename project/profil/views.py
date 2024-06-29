from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages

# Create your views here. 
def profi(request):
    pro=Profil.objects.all()
    profile={'pr1':pro}
    return render(request,'profile.html',profile)

def fprofil(request):
   
    if not request.user.is_authenticated:
        messages.info(request,'please login to access that page')
        return redirect('/authapp/login')
    if request.method =='POST': 
        name=request.POST.get('name')
        position=request.POST.get('position')
        selfdesc=request.POST.get('selfdesc')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        edu=request.POST.get('edu')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        pr=Profil(name=name,position=position,selfdesc=selfdesc,age=age,phone=phone,city=city,edu=edu,email=email,gender=gender)
        pr.save()
        return redirect(profi)
    return render(request,'fpro.html')