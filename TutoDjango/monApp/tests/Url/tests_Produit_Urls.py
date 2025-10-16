from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from monApp.views import ProduitListView, ProduitDetailView, ProduitCreateView, ProduitUpdateView, ProduitDeleteView
from monApp.models import Produit, Categorie, Statut

class ProduitUrlsTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        # Créer des objets nécessaires
        self.categorie = Categorie.objects.create(nomCat="Test Categorie")
        self.statut = Statut.objects.create(libelle="Test Statut")
        self.produit = Produit.objects.create(
            intituleProd="Test Produit",
            prixUnitaireProd=10.50,
            dateFabrication="2023-01-01",
            categorie=self.categorie,
            statut=self.statut
        )
    
    def test_produit_list_url_is_resolved(self):
        url = reverse('lst_prdts')  # ✅ Corrigé selon urls.py
        self.assertEqual(resolve(url).func.view_class, ProduitListView)
    
    def test_produit_detail_url_is_resolved(self):
        url = reverse('dtl-prdt', args=[self.produit.refProd])
        self.assertEqual(resolve(url).func.view_class, ProduitDetailView)
    
    def test_produit_create_url_is_resolved(self):
        url = reverse('crt-prdt')
        self.assertEqual(resolve(url).func.view_class, ProduitCreateView)
    
    def test_produit_update_url_is_resolved(self):
        url = reverse('prdt-chng', args=[self.produit.refProd])
        self.assertEqual(resolve(url).func.view_class, ProduitUpdateView)
    
    def test_produit_delete_url_is_resolved(self):
        url = reverse('dlt-prdt', args=[self.produit.refProd])
        self.assertEqual(resolve(url).func.view_class, ProduitDeleteView)
    
    def test_produit_list_response_code(self):
        response = self.client.get(reverse('lst_prdts'))  # ✅ Corrigé
        self.assertEqual(response.status_code, 200)
    
    def test_produit_detail_response_code(self):
        url = reverse('dtl-prdt', args=[self.produit.refProd])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_produit_detail_response_code_KO(self):
        url = reverse('dtl-prdt', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_produit_create_response_code_OK(self):
        response = self.client.get(reverse('crt-prdt'))
        self.assertEqual(response.status_code, 200)
    
    def test_produit_update_response_code_OK(self):
        url = reverse('prdt-chng', args=[self.produit.refProd])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_produit_update_response_code_KO(self):
        url = reverse('prdt-chng', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_produit_delete_response_code_OK(self):
        url = reverse('dlt-prdt', args=[self.produit.refProd])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_produit_delete_response_code_KO(self):
        url = reverse('dlt-prdt', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)