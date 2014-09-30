from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from lift_zone.forms import EmailForm


def enviar_correo(request):

    if request.method = "Post":

        forma = EmailForm(request.POST)

        if forma.is_valid():
            
            return HttpResponse("Todo OK")
