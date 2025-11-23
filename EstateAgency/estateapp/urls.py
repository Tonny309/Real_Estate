
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


    path('service-details/', views.servicedetails, name='service_details'),

    path('services/', views.services, name= 'services'),

    path('starterpage/', views.starterpage, name='starterpage'),

    path('property/<int:id>/', views.propertysingle, name='propertysingle'),



]
