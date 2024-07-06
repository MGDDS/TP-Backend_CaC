from .models import Pizzas
from .serializer import PizzaSerializer
from rest_framework import viewsets


class PizzaViewSet(viewsets.ModelViewSet):
    queryset=Pizzas.objects.all()
    serializer_class=PizzaSerializer