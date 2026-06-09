from importlib.resources import path

from django.urls import path
from .views import home

app_name = 'operadores'

urlpatterns = [
    path('', home)
]

