from django.shortcuts import render

# Create your views here.

def rohit(request):
    return render ( request,'rohit.html',context={'name':'Rohit Sharma','role':'captain of MI'})