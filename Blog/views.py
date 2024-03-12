from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def celsusar(request):
    return render(request,'blog/celsus_Ar.html')

def hacettepear(request):
    return render(request,'blog/hacettepe_Ar.html')
def blogs(request):
    return render(request,'blog/blogs.html')