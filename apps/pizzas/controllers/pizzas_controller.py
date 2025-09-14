from rest_framework.viewsets import ModelViewSet

from apps.pizzas.models.pizzas import Pizza
from apps.pizzas.schemas.pizza_schema import PizzaSerializer


class PizzasViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
