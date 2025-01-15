from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def hellomummy(request):
    return render(request,'hellomummy.html')
