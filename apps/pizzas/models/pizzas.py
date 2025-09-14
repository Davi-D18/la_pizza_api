from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pizzas/', blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Pizzas'

    def __str__(self):
        return self.name
