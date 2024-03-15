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
   
    ]