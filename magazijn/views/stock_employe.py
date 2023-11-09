from django.shortcuts import render

from django.views import View

from ..models import Product

class StockEmployeView(View):
    model = Product
    template_name = 'magazijn/stock-employe.html'

    def get(self, request):

        return render(request, self.template_name, {'products': self.model.objects.all()})

