from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseNotFound, \
    HttpResponseServerError
from django.shortcuts import render

def home(req: HttpRequest):
    if req.method == 'GET':
        return render(req, template_name =  'operadores/index.html')
    return HttpResponseNotAllowed(['GET'])

def somar(req: HttpRequest, a, b):
    soma = a + b
    return HttpResponse('<h1>A Soma e´:  {}</h1>'.format(soma))

def subtrair(req: HttpRequest, a, b):
    subtracao = a - b
    return HttpResponse('<h1>A Subtração é:  {}</h1>'.format(subtracao))

def multiplicar(req: HttpRequest, a, b):
    multiplicacao = a * b
    return HttpResponse('<h1>A Multiplicação é:  {}</h1>'.format(multiplicacao))

def dividir(req: HttpRequest, a, b):
    divisao = a / b
    return HttpResponse('<h1>A Divisão é:  {}</h1>'.format(divisao))