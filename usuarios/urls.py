from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import *
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'UsuariosJD', UsuariosJDViewSet)
router.register(r'PedidoJD', PedidoJDViewSet)
router.register(r'PerfilJorge', PerfilJorgeViewSet)
#router.register(r'UsuariosJorge', UsuariosJorgeViewSet)
router.register(r'ClienteRocha', ClienteRochaViewSet)
router.register(r'datos_privados', DatosPrivadosViewSet)
router.register(r'datos_privados_correo', DatosPrivadosCorreoViewSet)
router.register(r'datos_publicos_envios', EnvioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
