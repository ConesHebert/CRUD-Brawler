from django.db import models


    # CHOICES de raridade

GENERO_CHOICES = [
    ('RR', "Raro"),
    ('SR', "Super Raro"),
    ('EP', "Épico"),
    ('MT', "Mítico"),
    ('LD', "Lendario"),
]

class Brawlers(models.Model):
    Nome = models.CharField(max_length=100, verbose_name='Nome')
    starPowers = models.CharField(max_length=100, verbose_name='Star Power')
    gadgets = models.CharField(max_length=100, verbose_name='Gadget')
    raridade = models.CharField(max_length=100, verbose_name='Raridade', choices=RARIDADE_CHOICES)

    class Meta:
        verbose_name = 'Brawler'
        verbose_name_plural = 'Brawlers'
    def __str__(self):
        return self.Nome