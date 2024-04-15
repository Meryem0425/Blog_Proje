from plistlib import PlistFormat
from .models import *
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import *



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
            'name': product.name.capitalize(),
            'date': product.date,
            'image_url': image_url,
            
        })

    return JsonResponse({'products': data})


def admin(request):
    return render (request,'blog/admin.html')

def blog_listesi(request):
    blog = arama.objects.all()
    return render(request, 'admin_dashboard/blog_listesi.html', {'blog_list':blog})




def blog_olustur(request):
    return render(request,'admin_dashboard/blog_olustur.html')

def kullanıcı_listesi(request):
    return render(request,'admin_dashboard/kullanıcı_listesi.html')

def musteri_listesi(request):
    return render(request,'admin_dashboard/musteri_listesi.html')

def hosting_listesi(request):
    return render (request,'admin_dashboard/hosting_listesi.html')

def domain_listesi(request):
    return render (request,'admin_dashboard/domain_listesi.html')

def proje_olustur(request):
    return render (request,'admin_dashboard/proje_olustur.html')

def projeler_listesi(request):
    return render (request,'admin_dashboard/projeler_listesi.html')

def gorevler(request):
    return render (request,'admin_dashboard/gorevler.html')

def admin_hakkımızda(request):
    return render (request,'admin_dashboard/admin_hakkımızda.html')

def duzenle(request):
    return render (request,'blog_dashboard/duzenle.html')

def delete (request,blog_id):
    blog = arama.objects.get(pk=blog_id)
    blog.delete()
    return redirect("blog_listesi")

#"name","description","image","date","enddate","release_status"

def update(request, blog_id):
    if request.method == "POST":
        print(request.POST)
        form = ListForm(request.POST)
        if form.is_valid():
         blog_update=arama.objects.get(id=blog_id)
         blog_update.name=form.cleaned_data['name']
         blog_update.description = form.cleaned_data['description']
       
         blog_update.release_status=form.cleaned_data['release_status']
         blog_update.save()
         return redirect('blog_listesi')
        else:
            print(form.errors)
            return redirect('blog_listesi')
        
    else:
        update_data = arama.objects.get(pk=blog_id)
        update_image= update_data.image.url
        status_list={"Yayınlandı","Yayınlanmadı","Arşiv"}
        return render(request, 'admin_dashboard/duzenle.html', {'update_data': update_data,'update_image':update_image,'status_list':status_list})
    










        
    
    