from django.db import models

# Create your models here.

class Klant(models.Model):
    GezinsNaam = models.CharField(max_length=100)
    Volwassenen = models.IntegerField()
    Kinderen = models.IntegerField()
    Babies = models.IntegerField()
    Postcode = models.CharField(max_length=50)
    Varkesvlees = models.BooleanField()
    Vegataries = models.BooleanField()
    Veganistisch = models.BooleanField()
    Alergieën = models.ManyToManyField("Alergie", related_name="klant")

    def __str__(self):
        return self.GezinsNaam, self.id
    
class BSN(models.Model):
    Klant = models.ForeignKey("Klant", on_delete=models.DO_NOTHING, null=True)
    BSN = models.IntegerField()
    volledigeNaam = models.CharField(max_length=100)

    def __str__(self):
        return self.volledigeNaam, self.id
        
class Alergie(models.Model):
    Naam = models.CharField(max_length=100)

    def __str__(self):
        return self.Naam, self.id 