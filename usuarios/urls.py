from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import *
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'usuarios-jd', UsuariosJDViewSet)
router.register(r'pedidos-jd', PedidoJDViewSet)
router.register(r'perfil-jp', PerfilJorgeViewSet)
router.register(r'usuarios-jp', UsuariosJorgeViewSet)
router.register(r'clientes-r', ClienteRochaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
