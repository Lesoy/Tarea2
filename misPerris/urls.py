from django.contrib import admin
from django.urls import path
from .views import index, galeria, formulario,contacto

urlpatterns = [
    path('',index,name='IND'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORM'),
    path('contacto/',contacto,name='CONT'),
]
