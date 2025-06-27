from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Musicas



@admin.register(Musicas)
class listaBrawler(admin.ModelAdmin):
    list_display = ('nome', 'artista', 'album', 'genero')
    list_filter = ('artista',)


    
    # Tirar o registro
admin.site.unregister(User)
admin.site.unregister(Group)


