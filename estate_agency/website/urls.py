from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('properties/', views.properties, name='properties'),
    path('agents/', views.agents, name='agents'),
    path('contact/', views.contact, name='contact'),
    path('property-single/', views.property_single, name='property_single'),
    path('service-details/', views.service_details, name='service_details'),
    path('data-fetching/', views.data_fetching, name='data_fetching'),
    path('api/enquiries/', views.api_enquiries, name='api_enquiries'),
]
