from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import *
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'usuarios-jd', UsuarioViewSet)
router.register(r'pedidos-jd', PedidoViewSet)
router.register(r'perfil-jp', PerfilViewSet)
router.register(r'clientes-r', ClienteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
