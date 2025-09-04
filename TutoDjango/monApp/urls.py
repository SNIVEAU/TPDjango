from django.urls import path
from . import views
urlpatterns = [
 path("home/<param>", views.home, name="home"),
 path("about",views.about,name="about"),
 path("contact",views.contact, name="contact"),
 path("produits",views.ListProduits,name="produits"),
 path("statut",views.ListProduits,name="statut"),
 path("categories",views.ListProduits,name="categories")
]
