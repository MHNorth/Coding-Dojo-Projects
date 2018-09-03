from django.shortcuts import render


def CatalogHome(request):
        return render(request, 'catalog/index.html')   
