from rest_framework import serializers
from .models import Chocolate

class ChocolateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chocolate
        fields = '__all__'
