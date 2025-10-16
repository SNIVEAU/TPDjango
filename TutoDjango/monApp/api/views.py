from rest_framework import generics
from monApp.models import Categorie
from .serializers import CategorieSerializer

class CategorieAPIView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer