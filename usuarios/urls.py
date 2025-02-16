from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import UsuariosViewSet, ProductosViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'productos', ProductosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
