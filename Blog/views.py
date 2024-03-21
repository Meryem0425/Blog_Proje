import Blog
from .models import arama
from django.http import JsonResponse
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

def blog_sayfa(request):
    return render (request,'blog/blog_sayfa.html')    

def blog_details(request,blog_id):
    blog = arama.objects.get(id=blog_id)
    blog_id_my = blog.id
    blog_name = blog.name
    blog_detay= blog.description
    blog_tarih = blog.date# Tarih formatını istediğiniz gibi ayarlayın

    if blog.image:
        blog_resim = blog.image.url
    else:
        blog_resim = '/static/images/about.jpg'  # Sabit bir resim yolunu belirtin

    return render(request, 'blog/blog_detail.html', {'blog_id': blog_id_my, 'blog_name': blog_name, 'blog_detay': blog_detay, 'blog_resim': blog_resim ,'blog_tarih':blog_tarih})




def blogs(request):
    blogs=arama.objects.all()
    for blog in blogs:
        blog.date=blog.date  # Tarih formatını istediğiniz gibi ayarlayın
        if blog.image:
            blog.image= blog.image.url
        else:
            blog.image='/static/images/about.jpg'
       
    return render(request, 'blog/blogs.html',{'repeat_times':blogs})
from django.http import JsonResponse

def search_products(request):
    query = request.GET.get('query', '')
    products = arama.objects.filter(name__icontains=query)
    data = []
    for product in products:
        image_url = product.image.url if product.image else None
        data.append({
            'id': product.id,
            'name': product.name,
            'date': product.date,
            'image_url': image_url,
            
        })

    return JsonResponse({'products': data})
