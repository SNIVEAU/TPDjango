import datetime
from django.db import models

# Create your models here.
from django.db import models
class Categorie(models.Model):
	idCat = models.AutoField(primary_key=True)
	nomCat = models.CharField(max_length=100)

	def __str__(self):
		return self.nomCat

class Statut(models.Model):
	idStatut = models.AutoField(primary_key=True)
	libelle = models.CharField(max_length=20)

class Produit(models.Model):
	refProd = models.AutoField(primary_key=True)
	intituleProd = models.CharField(max_length=200)
	prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
	dateFabrication = models.DateField(default=datetime.date(2024, 9, 4))
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits", null=True, blank=True)
	statut = models.ForeignKey(Statut, on_delete=models.CASCADE, related_name="produits", null=True, blank=True)

	def __str__(self):
		return self.intituleProd
	
class Rayon(models.Model):
	refRayon = models.AutoField(primary_key=True)
	
	def __str__(self):
		return str(self.refRayon)

class Contenir(models.Model):
	pk = models.CompositePrimaryKey("refProd", "refRayon")

	refProd = models.ForeignKey(Produit, on_delete=models.CASCADE,related_name="produits",  blank=True)
	refRayon = models.ForeignKey(Rayon,on_delete=models.CASCADE,related_name="rayons",  blank=True)
	qte = models.IntegerField(default=None)
	