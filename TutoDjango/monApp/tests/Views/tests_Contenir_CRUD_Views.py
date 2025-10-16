from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from monApp.models import Produit, Rayon, Contenir, Categorie, Statut

class ContenirViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
        # Créer des objets nécessaires
        self.categorie = Categorie.objects.create(nomCat="Test Cat")
        self.statut = Statut.objects.create(libelle="Test Statut")
        self.rayon = Rayon.objects.create(nomRayon="Test Rayon")
        self.produit = Produit.objects.create(
            intituleProd="Test Produit",
            prixUnitaireProd=10.00,
            dateFabrication="2023-01-01",
            categorie=self.categorie,
            statut=self.statut
        )
        self.contenir = Contenir.objects.create(
            refProd=self.produit,
            refRayon=self.rayon,
            Qte=5
        )
    
    def test_contenir_create_view_get(self):
        response = self.client.get(reverse('cntnr-crt', args=[self.rayon.refRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/create_contenir.html')
    
    def test_contenir_update_qte_view_get(self):
        url = reverse('cntnr-updt-qte', args=[self.rayon.refRayon, self.produit.refProd])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_contenir_qte.html')
    
    def test_contenir_delete_view_get(self):
        url = reverse('cntnr-dlt', args=[self.rayon.refRayon, self.produit.refProd])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_contenir.html')
    
    def test_contenir_delete_view_post(self):
        url = reverse('cntnr-dlt', args=[self.rayon.refRayon, self.produit.refProd])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Contenir.objects.filter(
            refProd=self.produit,
            refRayon=self.rayon
        ).exists())