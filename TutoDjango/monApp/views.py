from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import Http404, HttpResponse
def home(request):
    if request.GET and request.GET["test"]:
        raise Http404
    string = request.GET["name"]
    return HttpResponse("Bonjour %s!" %string)

def about(request):
 return HttpResponse("<h1>A propos </h1>")

def contact(request):
 return HttpResponse("<p> Contact </p>")

def ListProduits(request):
    prdts = Produit.objects.all()
    html = """
            <h1> Produits
            <li>
            """
    for prod in prdts:
        html += "<ul> " + prod.intituleProd + "</ul>"

    html += "</li>"
    return HttpResponse(html)
    

def ListStatus(request):
    status = Statut.objects.all()
    html = """
            <h1> Statut
            <li>
            """
    for stat in status:
        html += "<ul> " + stat.libelle + "</ul>"

    html += "</li>"
    return HttpResponse(html)

def ListCategorie(request):
    categories = Categorie.objects.all()
    html = """
            <h1> Catégorie
            <li>
            """
    for cate in categories:
        html += "<ul> " + cate.nomCat + "</ul>"

    html += "</li>"
    return HttpResponse(html)