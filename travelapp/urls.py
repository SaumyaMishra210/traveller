from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about, name='about'),
    path('success', views.success, name='success'),
    path('contact', views.contact),
    path('new', views.book_details1, name='new'),
]
