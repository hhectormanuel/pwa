from django.urls import path
from .views import IndexView, ContactoView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'djangopwa'

urlpatterns =[
    path('index',IndexView.as_view(), name='index' ),
    path('contacto', ContactoView.as_view(), name='contacto')
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)