from django.shortcuts import render
from . import models
from .forms import DataForm
from django.contrib import messages
def home(request):
    Announcements=models.Announcements.objects.all().order_by('-id')[:4]
    updates=models.Announcements.objects.all() 
    return render(request,"home.html",{'Announcements':Announcements})



def announcement(request):
    Announcements=models.Announcements.objects.all().order_by('-id')[:4]
    return render(request,'Announcements.html',{'Announcements':announcements})
def leader(request):
    # Your logic here
    return render(request, 'leader.html')
def department(request):
    # Your logic here
    return render(request, 'department.html')

def application(request):
    if request.method=="POST":
     form=DataForm(request.POST or None,request.FILES)
     #incase form is validated
     if form.is_valid():
        form.save()
        messages.success(request,"you have successfully registered.")
        #clear the form
        form=DataForm()
        return render(request,"application.html",{'form':form})
     else:
        return render(request,"application.html",{'form':form})
    else:
        form=DataForm()
        return render(request,"application.html",{'form':form})