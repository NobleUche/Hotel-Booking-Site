from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('rooms',views.rooms,name='rooms'),
    path('services',views.services,name='services'),
    path('booking',views.booking,name='booking'),
]