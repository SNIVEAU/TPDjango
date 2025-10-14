from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from monApp.views import CategorieListView, CategorieDetailView, CategorieCreateView, CategorieUpdateView, CategorieDeleteView
from monApp.models import Categorie

class CategorieUrlsTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        self.ctgr = Categorie.objects.create(nomCat="Test Categorie")
    
    def test_categorie_list_url_is_resolved(self):
        url = reverse('lst_categories')
        self.assertEqual(resolve(url).func.view_class, CategorieListView)
    
    def test_categorie_detail_url_is_resolved(self):
        url = reverse('dtl-categorie', args=[1])
        self.assertEqual(resolve(url).func.view_class, CategorieDetailView)
    
    def test_categorie_create_url_is_resolved(self):
        url = reverse('crt-categorie')
        self.assertEqual(resolve(url).func.view_class, CategorieCreateView)
    
    def test_categorie_update_url_is_resolved(self):
        url = reverse('categorie-chng', args=[1])
        self.assertEqual(resolve(url).func.view_class, CategorieUpdateView)
    
    def test_categorie_delete_url_is_resolved(self):
        url = reverse('dlt-categorie', args=[1])
        self.assertEqual(resolve(url).func.view_class, CategorieDeleteView)
    
    def test_categorie_list_response_code(self):
        response = self.client.get(reverse('lst_categories'))
        self.assertEqual(response.status_code, 200)  # ✅ Maintenant ça marche
    
    def test_categorie_detail_response_code(self):
        url = reverse('dtl-categorie', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_categorie_detail_response_code_KO(self):
        url = reverse('dtl-categorie', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)  # ✅ Maintenant ça marche
    
    def test_categorie_create_response_code_OK(self):
        response = self.client.get(reverse('crt-categorie'))
        self.assertEqual(response.status_code, 200)
    
    def test_categorie_update_response_code_OK(self):
        url = reverse('categorie-chng', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_categorie_update_response_code_KO(self):
        url = reverse('categorie-chng', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_categorie_delete_response_code_OK(self):
        url = reverse('dlt-categorie', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_categorie_delete_response_code_KO(self):
        url = reverse('dlt-categorie', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_redirect_after_categorie_creation(self):
        response = self.client.post(
            reverse('crt-categorie'),
            data={'nomCat': 'Nouvelle Categorie'}
        )
        self.assertEqual(response.status_code, 302)
    
    def test_redirect_after_categorie_updating(self):
        response = self.client.post(
            reverse('categorie-chng', args=[self.ctgr.idCat]),
            data={'nomCat': 'Categorie Modifiee'}
        )
        self.assertEqual(response.status_code, 302)
    
    def test_redirect_after_categorie_deletion(self):
        response = self.client.post(reverse('dlt-categorie', args=[self.ctgr.pk]))
        self.assertEqual(response.status_code, 302)