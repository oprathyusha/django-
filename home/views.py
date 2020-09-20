from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib.messages import constants as messages
# Create your views here.
def index(request):
    context ={
        'variable':'This is a variable'
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact = Contact(name=name,email=email,phone=phone,date=datetime.today()) #object
        contact.save()
        messages.success(request, 'Profile details updated.')

       
    
    return render(request,'contact.html')