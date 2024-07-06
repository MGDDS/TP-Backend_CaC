from .models import Pizzas
from rest_framework import serializers

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzas
        fields = "__all__"