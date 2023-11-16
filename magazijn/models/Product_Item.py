from django.db import models

# Create your models here.
class ProductItem(models.Model):
    Product = models.ForeignKey("Product", on_delete=models.DO_NOTHING, null=True)
    leverings_datum = models.DateField(auto_now_add=True)
    leverancier = models.ForeignKey("directie.Leverancier", on_delete=models.DO_NOTHING, null=True)
    HoudsbaarheidDatum = models.DateField()
    Status = models.IntegerField()
    