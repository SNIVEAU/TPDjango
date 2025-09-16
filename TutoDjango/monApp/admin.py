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



class ProduitFilter(admin.SimpleListFilter):
    title = 'filtre produit'
    parameter_name = 'custom_status'

    def lookups(self, _, __):
        return (
            ('OnLine', 'En ligne'),
            ('OffLine', 'Hors ligne'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'OnLine':
            return queryset.filter(statut=1)
        if self.value() == 'OffLine':
            return queryset.filter(statut=0)
        return queryset

def set_Produit_online(modeladmin, request, queryset):
 queryset.update(statut=1)
set_Produit_online.short_description = "Mettre en ligne"
def set_Produit_offline(modeladmin, request, queryset):
 queryset.update(statut=0)
set_Produit_offline.short_description = "Mettre hors ligne"


class ProduitAdmin(admin.ModelAdmin):
    model = Produit
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "dateFabrication", "categorie", "statut"]
    list_editable = ["intituleProd", "prixUnitaireProd", "dateFabrication"]
    radio_fields = {"statut": admin.VERTICAL}
    search_fields = ('intituleProd', 'dateFabrication')
    list_filter = (ProduitFilter,)
    date_hierarchy = 'dateFabrication'
    ordering = ('-dateFabrication',)
    actions = [set_Produit_online, set_Produit_offline]

from decimal import Decimal, ROUND_HALF_UP

def prixTTCProd(instance):
    return (instance.prixUnitaireProd * Decimal('1.20')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
prixTTCProd.short_description = "Prix TTC"

admin.site.register(Produit, ProduitAdmin)  
admin.site.register(Categorie)
admin.site.register(Statut)
class RayonAdmin(admin.ModelAdmin):
    list_display = ('nomRayon',)
admin.site.register(Rayon,RayonAdmin)

