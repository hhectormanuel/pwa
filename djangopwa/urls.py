from django.urls import path
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'djangopwa'

urlpatterns =[
    path('index',IndexView.as_view(), name='index' )
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)