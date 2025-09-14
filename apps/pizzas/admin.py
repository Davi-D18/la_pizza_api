from django.contrib import admin

from apps.pizzas.models import Pizza

admin.site.site_header = "La Pizza Admin"
admin.site.site_title = "La Pizza Admin Portal"


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image')
    search_fields = ('name', 'description')
    list_filter = ('price',)
