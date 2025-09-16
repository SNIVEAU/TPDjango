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
    return render(request, 'monApp/about.html')

def contact(request):
    return render(request, 'monApp/contact.html')


# def ListProduits(request):
#     prdts = Produit.objects.all()
#     html = """
#             <h1> Produits
#             <li>
#             """
#     for prod in prdts:
#         html += "<ul> " + prod.intituleProd + "</ul>"

#     html += "</li>"
#     return HttpResponse(html)


def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})


def ListStatus(request):
    status = Statut.objects.all()
    
    return render(request, 'monApp/list_statuts.html',{'status': status})

def ListCategorie(request):
    categories = Categorie.objects.all()
    
    return render(request, 'monApp/list_categories.html',{'categories': categories})

def ListRayon(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html',{'rayons': rayons})
