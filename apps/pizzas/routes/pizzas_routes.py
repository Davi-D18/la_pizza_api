from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.pizzas.controllers.pizzas_controller import PizzasViewSet

router = DefaultRouter()
router.register('pizzas', PizzasViewSet)

urlpatterns = [
    path('', include(router.urls))
]
