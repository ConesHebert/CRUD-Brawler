from django.db import models


    # CHOICES de raridade

RARIDADE_CHOICES = [
    ('RR', "Raro"),
    ('SR', "Super Raro"),
    ('EP', "Épico"),
    ('MT', "Mítico"),
    ('LD', "Lendario"),
]

class Brawlers(models.Model):
    Nome = models.CharField(max_length=100, verbose_name='Nome')
    starPowers = models.CharField(max_length=100, verbose_name='Star Powers')
    gadgets = models.CharField(max_length=100, verbose_name='Gadgets')
    raridade = models.CharField(max_length=100, verbose_name='Raridade', choices=RARIDADE_CHOICES)

    class Meta:
        verbose_name = 'Brawler'
        verbose_name_plural = 'Brawlers'
    def __str__(self):
        return self.nome