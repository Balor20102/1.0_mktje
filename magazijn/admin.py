from django.contrib import admin

# Register your models here.

from .models import Product, ProductItem, Catagorie, Pakket

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'EAN', 'Varkesvlees', 'Vegataries', 'Veganistisch')
    list_filter = ('Varkesvlees', 'Vegataries', 'Veganistisch')
    search_fields = ('name', 'EAN')
    ordering = ['name']


class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('Product', 'Pakket', 'HoudsbaarheidDatum', 'Status')
    list_filter = ('Status',)
    search_fields = ('Product', 'Pakket')
    ordering = ['Product']


class CatagorieAdmin(admin.ModelAdmin):
    list_display = ('Naam', 'Omschrijving')
    list_filter = ('Naam',)
    search_fields = ('Naam',)
    ordering = ['Naam']

class PakketAdmin(admin.ModelAdmin):
    list_display = ('GezinsNaam', 'UitgiftDatum')
    list_filter = ('GezinsNaam',)
    search_fields = ('GezinsNaam',)
    ordering = ['GezinsNaam']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(Catagorie, CatagorieAdmin)
admin.site.register(Pakket, PakketAdmin)
