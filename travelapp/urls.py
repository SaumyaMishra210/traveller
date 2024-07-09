from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('destination', views.destination, name='destination'),
    path('guide', views.guide, name='guide'),
    path('package/', views.package, name='package'),
    path('service/', views.service, name='service'),
    path('single', views.single, name='single'),
    path('success/', views.success, name='success'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('new/', views.book_details1, name='new'),
    path('login',views.login,name='login'),
    path('register',views.register,name ='register'),
]
