from rest_framework import serializers
from ..models import Categorie

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ["idCat", "nomCat"]
    