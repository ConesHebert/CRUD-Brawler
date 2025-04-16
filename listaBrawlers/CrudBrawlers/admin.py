from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Brawlers



@admin.register(Brawlers)
class listaBrawler(admin.ModelAdmin):
    list_display = ("Nome",'starPowers','gadgets','raridade')
    list_filter = ['raridade']

    
    # Tirar o registro
admin.site.unregister(User)
admin.site.unregister(Group)


