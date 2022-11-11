from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'index3.html', context)