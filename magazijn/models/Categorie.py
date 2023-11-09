from django.db import models

class Catagorie(models.Model):
        Naam = models.CharField(max_length=100)
        Omschrijving = models.CharField(max_length=100)

        def __str__(self):
            return self.Naam