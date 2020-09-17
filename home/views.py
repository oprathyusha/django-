from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context ={
        'variable':'This is a variable'
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse ('Hi this is Prathyusha!')

def services(request):
    return HttpResponse ('This is services page')

def contact(request):
    return HttpResponse ('contact - xyz@gmail.com')