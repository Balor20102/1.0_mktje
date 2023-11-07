from django.db import models

# Create your models here.

class Product(models.model):
    name = models.CharField(max_length=100)
    EAN = models.IntegerField()
    Afbeelding = models.ImageField()
    Varkesvlees = models.BooleanField()
    Vegataries = models.BooleanField()
    Veganistisch = models.BooleanField()
    Catagorieën = models.ManyToManyField("Catagorie", related_name="product")

    def __str__(self):
        return self.name, self.id
    
class ProductItem(models.model):
    Product = models.ForeignKey("Product", on_delete=models.DO_NOTHING, null=True)
    Pakket = models.ForeignKey("Pakket", on_delete=models.DO_NOTHING, null=True)
    HoudsbaarheidDatum = models.DateField()
    Status = models.IntegerField()
    

    class Catagorie(models.model):
        Naam = models.CharField(max_length=100)
        Omschrijving = models.CharField(max_length=100)

        def __str__(self):
            return self.Naam, self.id
        
    class Pakket(models.model):
        GezinsNaam = models.ForeignKey("Klant", on_delete=models.DO_NOTHING, null=True)
        UitgiftDatum = models.DateField()

        def __str__(self):
            return self.GezinsNaam, self.id
