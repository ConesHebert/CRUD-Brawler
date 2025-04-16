from django.contrib import admin
from .models import Brawlers



@admin.register(Brawlers)
class listaBrawler(admin.ModelAdmin):
    list_display = ("Nome",'starPowers','gadgets','raridade')
    list_filter = ['raridade']

    
    # Tirar o registro
    # admin.site.unregister(Brawlers)


