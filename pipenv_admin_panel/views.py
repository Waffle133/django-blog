"""Vistas del proyecto"""
# Utilities
from datetime import datetime
import json
# Django
from django.http import HttpResponse
from django.http import JsonResponse


def hello_world(request):
    return HttpResponse('Hello world!')


def server_hour(request):
    now = str(datetime.now().strftime('%d/%m/%Y '))
    return HttpResponse('Hola! La fecha del servidor es {now}'.format(now=now))


def test_request(request):
    numbers = sorted(map(int, request.GET["numbers"].split(",")))
    data = {
        'status': 'success',
        'numbers': numbers,
        'message': 'Enteros sorteados de manera correcta'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    # return JsonResponse(data, safe=False)


def test_path_converter(request, name, age, year):
    if age < 18:
        message = 'Hola, {}. No tienes permitido entrar a este sitio'.format(name)
    else:
        message = "Bienviado(a), {}. Es bueno verte por aquí".format(name)
    return HttpResponse(message)
