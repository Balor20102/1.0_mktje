from django.db import models

# Create your models here.
class ProductItem(models.Model):
    Product = models.ForeignKey("Product", on_delete=models.DO_NOTHING, null=True)
    Pakket = models.ForeignKey("Pakket", on_delete=models.DO_NOTHING, null=True)
    HoudsbaarheidDatum = models.DateField()
    Status = models.IntegerField()
    