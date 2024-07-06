from django.db import models

# Create your models here.
class Pizzas(models.Model):
    
    class Meta:
        db_table = 'pizza_mysql'
    
    nombre = models.CharField(max_length=200, unique=True)
    
    tamanio = models.CharField(max_length=200)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre