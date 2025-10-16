from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from monApp.models import Produit, Categorie, Statut

class ProduitCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
        self.categorie = Categorie.objects.create(nomCat="Test Cat")
        self.statut = Statut.objects.create(libelle="Test Statut")

    def test_produit_create_view_get(self):
        response = self.client.get(reverse('crt-prdt'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/create_produit.html')

    def test_produit_create_view_post_valid(self):
        data = {
            "intituleProd": "ProduitPourTestCreation",
            "prixUnitaireProd": 15.99,
            "dateFabrication": "2023-01-01",
            "categorie": self.categorie.idCat,
            "statut": self.statut.idStatut
        }
        response = self.client.post(reverse('crt-prdt'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Produit.objects.count(), 1)
        self.assertEqual(Produit.objects.last().intituleProd, 'ProduitPourTestCreation')

class ProduitDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
        self.categorie = Categorie.objects.create(nomCat="Test Cat")
        self.statut = Statut.objects.create(libelle="Test Statut")
        self.produit = Produit.objects.create(
            intituleProd="ProduitPourTestDetail",
            prixUnitaireProd=20.00,
            dateFabrication="2023-01-01",
            categorie=self.categorie,
            statut=self.statut
        )

    def test_produit_detail_view(self):
        response = self.client.get(reverse('dtl-prdt', args=[self.produit.refProd]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_produit.html')
        self.assertContains(response, 'ProduitPourTestDetail')