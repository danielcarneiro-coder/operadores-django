from django.urls import path
from .views import home, somar, subtrair, multiplicar, dividir


app_name = 'operadores'

urlpatterns = [
    path('', home, name='home'),
    path('somar/<int:a>/<int:b>/', somar, name='somar'),
    path('subtrair/<int:a>/<int:b>/', subtrair, name='subtrair'),
    path('multiplicar/<int:a>/<int:b>/', multiplicar, name='multiplicacao'),
    path('dividir/<int:a>/<int:b>/', dividir, name='divisao')
 ]

