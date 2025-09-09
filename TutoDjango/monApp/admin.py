from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class ProduitInline(admin.TabularInline):
    model = Produit
    extra = 1 # nombre de lignes vides par défaut
class CategorieAdmin(admin.ModelAdmin):
    model = Categorie
    inlines = [ProduitInline]
class ProduitAdmin(admin.ModelAdmin):
    model = Produit
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "dateFabProd", "categorie", "status"]
    list_editable = ["intituleProd", "prixUnitaireProd", "dateFabProd"]
    radio_fields = {"status": admin.VERTICAL}

admin.site.register(Produit, ProduitAdmin)  
admin.site.register(Categorie)
admin.site.register(Statut)
class RayonAdmin(admin.ModelAdmin):
    list_display = ('nomRayon',)
admin.site.register(Rayon,RayonAdmin)
admin.site.register(Contenir)

