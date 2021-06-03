from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def galeria(request):
    return render(request,'galeria.html')

def formulario(request):
    return render(request,'formulario.html')

def contacto(request):
    return render(request, 'form_contacto.html')