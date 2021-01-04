from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse ('HOME')
    return render(request,'about.html')

def Home(request):
    #return HttpResponse ('hi sajad')
    return render(request,'Home.html')
