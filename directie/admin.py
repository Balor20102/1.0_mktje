from django.contrib import admin

# Register your models here.

from .models import Leverancier

class LeverancierAdmin(admin.ModelAdmin):
    list_display = ('BedrijfsNaam', 'Adres', 'LeveringsDatum', 'ContactPersoon', 'Telefoon', 'Email')
    list_filter = ('BedrijfsNaam',)
    search_fields = ('BedrijfsNaam',)
    ordering = ['BedrijfsNaam']

admin.site.register(Leverancier, LeverancierAdmin)