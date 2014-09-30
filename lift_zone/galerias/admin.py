from django.contrib import admin
from galerias.models import Galeria, Imagen


class GaleriaAdmin(admin.ModelAdmin): #{
	pass
#}

class ImagenAdmin(admin.ModelAdmin): #{
	pass
#}

admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Imagen, ImagenAdmin)