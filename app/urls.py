from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about.html', views.about),
    path('contact.html', views.contact),
    path('patients.html', views.patients),
    path('services.html', views.services),

]