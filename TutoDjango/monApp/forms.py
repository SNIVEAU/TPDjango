from django import forms
from .models import *
class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        #fields = '__all__'
        exclude = ('categorie', 'status')

class RayonForm(forms.ModelForm):
    class Meta:
        model = Rayon
        fields = '__all__'

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'

class ContenirForm(forms.ModelForm):
    Qte = forms.CharField(required=True)

    class Meta:
        model = Produit
        fields = '__all__'

# Formulaire pour modifier uniquement la quantité
class ContenirUpdateQteForm(forms.ModelForm):
    class Meta:
        model = Contenir
        fields = ['Qte']
        widgets = {
            'Qte': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'})
        }

# Formulaire pour modifier le produit (basé sur Produit avec quantité)
class ContenirUpdateProduitForm(forms.ModelForm):
    Qte = forms.IntegerField(min_value=0, label="Quantité dans le rayon", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Produit
        fields = ['intituleProd', 'prixUnitaireProd', 'dateFabrication', 'categorie', 'statut']
        widgets = {
            'intituleProd': forms.TextInput(attrs={'class': 'form-control'}),
            'prixUnitaireProd': forms.NumberInput(attrs={'class': 'form-control'}),
            'dateFabrication': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }
