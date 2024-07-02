from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('singup', views.signUpFormData ),
    # path('booking', views.bookingformdata),
    path('about',views.about ),
    # path('blog',views.blog),
 ]
