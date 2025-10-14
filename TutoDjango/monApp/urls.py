# from django.urls import path
# from . import views
# urlpatterns = [
#  path("home", views.home, name="home"),
#  path("about",views.about,name="about"),
#  path("contact",views.contact, name="contact"),
#  path("produits",views.ListProduits,name="produits"),
#  path("statut",views.ListStatus,name="statut"),
#  path("categories",views.ListCategorie,name="categories"),
#  path("rayons",views.ListRayon,name="rayons")
# ]
from django.urls import path
from . import views
from django.views.generic import *
urlpatterns = [
#path("home", views.home, name="home"),

#Route vers les listes de tables du models
path("home/", views.HomeView.as_view(),name="home"),
path("about",views.AboutView.as_view()),
path("contact",views.ContactView),
path("produits/",views.ProduitListView.as_view(),name="lst_prdts"),
path("statut",views.StatutListView.as_view()),
path("categories",views.CategorieListView.as_view(),name="lst_categories"),
path("rayons",views.RayonsListView.as_view(),name="lst_rayons"),
path('login/', views.ConnectView.as_view(), name='login'),
path('register/', views.RegisterView.as_view(), name='register'),
path('logout/', views.DisconnectView.as_view(), name='logout'),
path('email-sent/', TemplateView.as_view(template_name='monApp/email-sent.html'), name='email-sent'),
path("produit/",views.ProduitCreateView.as_view(), name="crt-prdt"),
path("produit/<pk>/update/",views.ProduitUpdateView.as_view(), name="prdt-chng"),
path("produit/<pk>/delete/",views.ProduitDeleteView.as_view(), name="dlt-prdt"),
path("rayon/", views.RayonCreateView.as_view(),name="crt-ray"),
path("rayon/<pk>/update/",views.RayonUpdateView.as_view(),name="ray-chng"),
path("rayon/<pk>/delete/",views.RayonDeleteView.as_view(),name="dlt-ray"),

path("categorie/", views.CategorieCreateView.as_view(), name="crt-categorie"),
path("categorie/<pk>/", views.CategorieDetailView.as_view(), name="dtl-categorie"),
path("categorie/<pk>/update/", views.CategorieUpdateView.as_view(), name="categorie-chng"),
path("categorie/<pk>/delete/", views.CategorieDeleteView.as_view(), name="dlt-categorie"),


path('rayon/<pk>/cntnr', views.ContenirCreateView.as_view(), name='cntnr-crt'),


#Route vers les détails

path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl-prdt"),
path("rayon/<pk>/",views.RayonDetailView.as_view(),name="dtl_rayon"),
# # Ancienne manière de gérer les urls en appelant une route
# path("statut",views.ListStatus,name="statut"),
# path("categories",views.ListCategorie,name="categories"),
# path("rayons",views.ListRayon,name="rayons")
]
