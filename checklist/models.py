from django.db import models

class Card(models.Model):
    # ABILITY_CHOICES = []

    poke_name = models.CharField(max_length=12)
    # image = models.ImageField()
    dexid = models.PositiveSmallIntegerField()
    # type1 = models.CharField(max_length=12)
    # type2 = models.CharField(max_length=12)
    # abilities = models.CharField(max_length=12, choices=ABILITY_CHOICES)

    
    def __str__(self):
        return self.poke_name