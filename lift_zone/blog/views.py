from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post
from lift_zone.forms import EmailForm


def index(request):
    
    forma_contacto = EmailForm()
    noticias = Post.objects.filter(estado = 'a', destacado = True).order_by('-creado')[:3]
    context = {
        'noticias'       : noticias,
        'forma_contacto' : forma_contacto,
    }

    return render(request, 'blog/index.html', context)
