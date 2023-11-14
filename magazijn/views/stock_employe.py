from django.shortcuts import render

from django.views import View

from ..models import Product

from ..filters import ProductFilter

class StockEmployeView(View):
    model = Product
    filterset_class = ProductFilter
    template_name = 'magazijn/stock-employe.html'

    def get(self, request):
        
        context = {
            'filter': self.filterset_class(request.GET, queryset=self.model.objects.all()),
        }

        return render(request, self.template_name, context )

