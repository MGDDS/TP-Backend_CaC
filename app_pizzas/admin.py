from django.contrib import admin
from .models import Pelicula

@admin.register(Pizzas)
class PizzasAdmin(admin.ModelAdmin):
    pass

# Register your models here.
