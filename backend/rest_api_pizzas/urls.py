
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lista-de-pizzas/", include("app_pizzas.urls"))
]
