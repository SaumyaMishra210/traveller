from django.urls import path
from . import views

urlpatterns = [
    # path("",views.index),
    path('about',views.about, name="hello"),
    path('blog',views.blog),
    path('',views.signUpFormData),
    # path('form',views.signUpFormData),
]
