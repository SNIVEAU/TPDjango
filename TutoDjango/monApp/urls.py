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
path("categories",views.CategorieListView.as_view()),
path("rayons",views.RayonsListView.as_view(),name="lst_rayons"),
path('login/', views.ConnectView.as_view(), name='login'),
path('register/', views.RegisterView.as_view(), name='register'),
path('logout/', views.DisconnectView.as_view(), name='logout'),
path('email-sent/', TemplateView.as_view(template_name='monApp/email-sent.html'), name='email-sent'),

#Route vers les détails

path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
path("rayon/<pk>/",views.RayonDetailView.as_view(),name="dtl_rayon"),
# # Ancienne manière de gérer les urls en appelant une route
# path("statut",views.ListStatus,name="statut"),
# path("categories",views.ListCategorie,name="categories"),
# path("rayons",views.ListRayon,name="rayons")
]
