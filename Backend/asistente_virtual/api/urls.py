from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, InteraccionViewSet, RegistroUsuarioView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'interacciones', InteraccionViewSet)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Autenticación con usuario/correo
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),  # Registro de usuarios
    path('', include(router.urls)),
]
