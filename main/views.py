from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
from django.forms.models import model_to_dict
import qrcode

def pokemon_specific(request, id):

    try:
        poke = Pokemon.objects.get(pid=id)
    except:
        return HttpResponse(status=404)

    returned = {}
    returned['name'] = poke.name
    returned['pid'] = poke.pid
    returned['qr_code'] = poke.qr_code
    returned['qr_url'] = poke.qr_code_image.url

    return render(request, 'main.html', {'pokemon': model_to_dict(poke)})

def index(request):

    try:
        poke = Pokemon.objects.get(pid=722)
    except:
        return HttpResponse(status=404)

    returned = {}
    returned['name'] = poke.name
    returned['pid'] = poke.pid
    returned['qr_code'] = poke.qr_code
    returned['qr_url'] = poke.qr_code_image.url

    return render(request, 'main.html', {'pokemon': model_to_dict(poke)})