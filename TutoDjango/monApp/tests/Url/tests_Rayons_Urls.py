from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from monApp.views import RayonsListView, RayonDetailView, RayonCreateView, RayonUpdateView, RayonDeleteView
from monApp.models import Rayon

class RayonUrlsTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.rayon = Rayon.objects.create(nomRayon="Test Rayon")
    
    def test_rayon_list_url_is_resolved(self):
        url = reverse('lst_rayons')  # ✅ Selon urls.py
        self.assertEqual(resolve(url).func.view_class, RayonsListView)
    
    def test_rayon_detail_url_is_resolved(self):
        url = reverse('dtl_rayon', args=[self.rayon.refRayon])
        self.assertEqual(resolve(url).func.view_class, RayonDetailView)
    
    def test_rayon_create_url_is_resolved(self):
        url = reverse('crt-ray')
        self.assertEqual(resolve(url).func.view_class, RayonCreateView)
    
    def test_rayon_update_url_is_resolved(self):
        url = reverse('ray-chng', args=[self.rayon.refRayon])
        self.assertEqual(resolve(url).func.view_class, RayonUpdateView)
    
    def test_rayon_delete_url_is_resolved(self):
        url = reverse('dlt-ray', args=[self.rayon.refRayon])
        self.assertEqual(resolve(url).func.view_class, RayonDeleteView)
    
    def test_rayon_list_response_code(self):
        response = self.client.get(reverse('lst_rayons'))
        self.assertEqual(response.status_code, 200)
    
    def test_rayon_detail_response_code(self):
        url = reverse('dtl_rayon', args=[self.rayon.refRayon])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_rayon_detail_response_code_KO(self):
        url = reverse('dtl_rayon', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_rayon_create_response_code_OK(self):
        response = self.client.get(reverse('crt-ray'))
        self.assertEqual(response.status_code, 200)
    
    def test_rayon_update_response_code_OK(self):
        url = reverse('ray-chng', args=[self.rayon.refRayon])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_rayon_update_response_code_KO(self):
        url = reverse('ray-chng', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_rayon_delete_response_code_OK(self):
        url = reverse('dlt-ray', args=[self.rayon.refRayon])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_rayon_delete_response_code_KO(self):
        url = reverse('dlt-ray', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)