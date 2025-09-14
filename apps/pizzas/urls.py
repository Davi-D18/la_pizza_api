from django.urls import path, include


urlpatterns = [
    path('', include('apps.pizzas.routes.pizzas_routes')),
]
