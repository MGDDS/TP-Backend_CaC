from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import PizzaViewSet

router=DefaultRouter()
router.register('pizza', PizzaViewSet, basename="pizza")

urlpatterns = [
    path('', include(router.urls)) # rutas generadas automaticamente
]