from monApp.api import views
from django.urls import include, path
urlpatterns = [
    path('categories/',views.CategorieAPIView.as_view(),name="api-lst-ctgrs"),
    path("api/", include("monApp.api.urls")), # routes API regroupées

    ]
