# -*- encoding: utf-8 -*-

from django.db import models



class Categoria(models.Model):
    
    nombre      = models.CharField(max_length = 100)
    descripcion = models.TextField(u'descripción')
    creado      = models.DateTimeField(u'fecha de creación', auto_now_add = True)
    modificado  = models.DateTimeField(u'última modificación', auto_now = True)

    def __unicode__(self):
        
        return self.nombre


class Tag(models.Model):
    
    nombre      = models.CharField(max_length = 100)
    descripcion = models.TextField(u'descripción')
    creado      = models.DateTimeField(u'fecha de creación', auto_now_add = True)
    modificado  = models.DateTimeField(u'última modificación', auto_now = True)

    def __unicode__(self):

        return self.nombre


class Post(models.Model):

    ESTADOS = (
        ('b', 'borrador'),
        ('p', 'aprobacíon pendiente'),
        ('a', 'aprobado'),
    )
    
    categoria  = models.ForeignKey(Categoria)
    Tags       = models.ManyToManyField(Tag, null = True, blank = True)
    titulo     = models.CharField(max_length = 255)
    contenido  = models.TextField()
    estado     = models.CharField(max_length = 1, default = 'b', choices = ESTADOS)
    destacado  = models.BooleanField(default = False)
    creado     = models.DateTimeField(u'fecha de creación', auto_now_add = True)
    modificado = models.DateTimeField(u'última modificación', auto_now = True)

    def __unicode__(self):

        return self.titulo


class Comentario(models.Model):

    email      = models.EmailField(max_length = 80)
    comentario = models.TextField()
    aprobado   = models.BooleanField(default = False)
    creado     = models.DateTimeField(u'fecha de creación', auto_now_add = True)
    modificado = models.DateTimeField(u'última modificación', auto_now = True)

    def __unicode__(self):

        return self.email

