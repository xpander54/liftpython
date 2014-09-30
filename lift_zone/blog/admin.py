from django.contrib import admin
from blog.models import Post, Categoria, Tag, Comentario


class PostAdmin(admin.ModelAdmin):
    pass

class CategoriaAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class ComentarioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comentario, ComentarioAdmin)
