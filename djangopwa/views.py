from django.shortcuts import render
from django.views.generic import View
import requests

 

# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'index3.html', context)


class ContactoView(View):
    def get(self, request, *args, **kwargs):
        url ="https://api-comida.onrender.com/contactoo/"
        r = requests.get(url)
        context = {
            "mensajes" : r.json()
        }
        return render(request, 'contacto.html', context)