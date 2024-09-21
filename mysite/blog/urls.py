from django.urls import path
from . import views

urlpatterns = [
    path('category-detail/<str:slug>/', views.category_detail, name='category_detail'),
    path('blog-details/<str:slug>', views.blog_details, name='blog_details'),
    path('tag-detail/<str:slug>/', views.tag_detail, name='tag_detail'),
    path('contact/', views.contact, name='contact'),
    # path('contact-form/', views.contact_form, name='contact_form'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('', views.home, name='home'),
    
]


