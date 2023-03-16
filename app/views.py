from django.shortcuts import render

# Create your views here.

def first(request):
    d={'name':'ASHU','age':3}
    return render(request,'sample.html',context=d)
