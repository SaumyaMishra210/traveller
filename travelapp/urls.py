from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about, name='about'),
    path('success', views.success , name = 'success'),
    path('contact', views.contact),
    path('newform',views.formView,name ='newform'),
    # path('singup', views.signUpFormData ),
    # path('booking', views.bookingformdata),
    path('new',views.book_details1 ,name = 'new'),
]
