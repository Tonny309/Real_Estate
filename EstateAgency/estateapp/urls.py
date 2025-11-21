
from django.contrib import admin
from django.urls import path
from estateapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('about/', views.about, name='about'),
    path('agents/', views.agents, name='agents'),

    path('contact/', views.contact, name='contact'),

    path('', views.index, name='index'),

    path('properties/', views.properties, name='properties'),

    path('propertysingle/', views.propertysingle, name='propertysingle'),

    path('servicedetails/', views.servicedetails, name='servicedetails'),

    path('services/', views.services, name= 'services.html'),

    path('starterpage', views.starterpage, name='starterpage'),


]
