from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('celsusAr/',views.celsusar, name="celsusAr"),
    path('hacettepeAr/',views.hacettepear, name="hacettepear"),
    path('blogs/',views.blogs, name="blogs"),
    path('blog_detail/<int:blog_id>/',views.blog_details, name="blog_detail"),
    path('search_products/', views.search_products, name='search_products'),

    path('blog/admin/',views.admin,name="admin"),
    path('blog/admin/blog_listesi',views.blog_listesi,name="blog_listesi"),
    path('blog/admin/blog_olustur',views.blog_olustur,name="blog_olustur"),
    path('blog_guncelleme_sayfası',views.blog_guncelleme_sayfası,name="blog_guncelleme_sayfası"),
    path('blog/admin/kullanıcı_listesi',views.kullanıcı_listesi,name="kullanıcı_listesi"),
    path('blog/admin/musteri_listesi',views.musteri_listesi,name="musteri_listesi"),
    path('blog/admin/hosting_listesi',views.hosting_listesi,name="hosting_listesi"),
    path('blog/admin/domain_listesi',views.domain_listesi,name="domain_listesi"),
    path('blog/admin/projeler_listesi',views.projeler_listesi,name="projeler_listesi"),
    path('blog/admin/proje_olustur',views.proje_olustur,name="proje_olustur"),
    path('blog/admin/gorevler',views.gorevler,name="gorevler"),
    path('blog/admin/admin_hakkımızda',views.admin_hakkımızda,name="admin_hakkımızda"),
    path('delete/<int:blog_id>/',views.delete,name="delete"),
    path('update/<int:blog_id>/',views.update, name="update"),
    path('blog/admin/duzenle',views.duzenle,name="duzenle"),
    

    ]