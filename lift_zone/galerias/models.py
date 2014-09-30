# -*- encoding: utf-8 -*-

from django.db import models

from blog.models import Post


class Galeria(models.Model): #{


	post        = models.ForeignKey(Post)
	nombre      = models.CharField(max_length = 255)
	descripcion = models.TextField(blank = True)
	creado      = models.DateTimeField(u'fecha de creación', auto_now_add = True)
	modificado  = models.DateTimeField(u'última modifiación', auto_now = True)


	def __unicode__(self): #{

		return self.nombre

	#}


	class Meta: #{

		verbose_name = u'galería'
		verbose_name_plural = u'galerías'

	#}


#}


class Imagen(models.Model): #{
	

	galeria     = models.ForeignKey(Galeria, verbose_name = u'galería')
	imagen      = models.ImageField(upload_to = 'galerias')
	descripcion = models.TextField(u'descripción', blank = True)
	creado      = models.DateTimeField(u'fecha de upload', auto_now_add = True)


	def __unicode__(self): #{

		return self.galeria

	#}


	class Meta: #{

		verbose_name_plural = u'imágenes'

	#}

#}
