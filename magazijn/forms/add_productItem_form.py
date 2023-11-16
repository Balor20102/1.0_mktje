from django import forms
from ..models import ProductItem
from ...directie import models

class ProductItemForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = [ 'HoudsbaarheidDatum', 'leverancier']
        widgets = {
            'HoudsbaarheidDatum': forms.DateInput(attrs={'class': 'form-control'}),
            'leverancier': forms.ModelMultipleChoiceField(queryset=models.Leverancier.objects.all(), widget=forms.CheckboxSelectMultiple)
        }