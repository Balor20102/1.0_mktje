from django.db import models

# Create your models here.
class Leverancier(models.Model):
    BedrijfsNaam = models.CharField(max_length=100)
    Adres = models.CharField(max_length=100)
    ContactPersoon = models.CharField(max_length=100)
    Telefoon = models.IntegerField()
    Email = models.EmailField()
    LeveringsDatum = models.DateField()