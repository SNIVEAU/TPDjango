from django.shortcuts import render
from .models import *
from django.views.generic import *

# Create your views here.
from django.http import Http404, HttpResponse

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)
class ContactView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['titreh1'] = "Nous contacter"
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)
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

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    def get_queryset(self ) :
        return Produit.objects.order_by("prixUnitaireProd")
    
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
    
class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "status"
    def get_queryset(self ) :
        return Statut.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes Statuts"
        return context

class RayonsListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"
    def get_queryset(self ) :
        return Rayon.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(RayonsListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        return context


class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "categories"
    def get_queryset(self ) :
        return Categorie.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories"
        return context

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        return context

#  # Ancienne version de gestion des vues en faisant un render du template
# def ListStatus(request):
#     status = Statut.objects.all()
    
#     return render(request, 'monApp/list_statuts.html',{'status': status})

# def ListCategorie(request):
#     categories = Categorie.objects.all()
    
#     return render(request, 'monApp/list_categories.html',{'categories': categories})

# def ListRayon(request):
#     rayons = Rayon.objects.all()
#     return render(request, 'monApp/list_rayons.html',{'rayons': rayons})
