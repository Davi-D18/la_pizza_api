from rest_framework import serializers
from apps.pizzas.models.pizzas import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'
