from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('singup', views.signUpFormData ),
    # path('booking', views.bookingformdata),
    path('about',views.about,name = 'about' ),
    # path('new/',views.book_details1),
    # path('blog',views.blog),
 ]
