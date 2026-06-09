from django.http import HttpRequest, HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseNotFound, \
    HttpResponseServerError
from django.shortcuts import render


def home(req: HttpRequest):
    if req.method == 'GET':
        return render(req, template_name =  'operadores/index.html')