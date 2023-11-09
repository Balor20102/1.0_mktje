from django.db import models
        
class Pakket(models.Model):
        GezinsNaam = models.ForeignKey("Klanten.Klant", on_delete=models.DO_NOTHING, null=True)
        UitgiftDatum = models.DateField()

        def __str__(self):
            return self.GezinsNaam
