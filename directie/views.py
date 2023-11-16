from django.shortcuts import render, redirect
from directie.forms import createcategorieënform
from magazijn.models import Catagorie
from django.shortcuts import get_object_or_404

# Create your views here.

def create_catagorie(request):
    if request.method == 'POST':
        form = createcategorieënform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directiehomepage')  # Redirect to a success page or another view
    else:
        form = createcategorieënform()

    return render(request, 'directie/Categorieëtoevoegen.html', {'form': form})

def catagorieën(request):
    catagorieën = Catagorie.objects.all()
    context = {'catagorieen': catagorieën}
    return render(request, 'directie/Categorieënoverzicht.html', context)

def directiehomepage(request):
    return render(request, 'directie/homepagina.html')

def verwijder_catagorie(request, char_field_value):
    obj = get_object_or_404(Catagorie, char_field=char_field_value)
    obj.delete()
    catagorieën = Catagorie.objects.all()
    context = {'catagorieen': catagorieën}
    return render(request, 'directie/Categorieënoverzicht.html', context)