
from django.shortcuts import render
from store.models import Produit


def home(request):
    produits=Produit.objects.all()
    context={"produits":produits}
    return render(request,"home.html",context)