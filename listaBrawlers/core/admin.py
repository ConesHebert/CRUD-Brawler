from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Musicas



@admin.register(Musicas)
class listaBrawler(admin.ModelAdmin):
    list_display = ("Nome",'Artista','Album','Genero')
    list_filter = ['Artista']

    
    # Tirar o registro
admin.site.unregister(User)
admin.site.unregister(Group)


