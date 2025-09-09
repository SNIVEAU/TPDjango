from django.urls import path
from . import views
urlpatterns = [
 path("home", views.home, name="home"),
 path("about",views.about,name="about"),
 path("contact",views.contact, name="contact"),
 path("produits",views.ListProduits,name="produits"),
 path("statut",views.ListStatus,name="statut"),
 path("categories",views.ListCategorie,name="categories")
]
