from django.contrib import admin
from .models import Pizzas

@admin.register(Pizzas)
class PizzasAdmin(admin.ModelAdmin):
    pass

# Register your models here.
