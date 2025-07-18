from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('contact/', views.contact_page, name='contactform'),
    path('success-page/', views.success_page, name='success-page'),
]
