from rest_framework import viewsets
from .models import Usuario, Interaccion
from .serializers import UsuarioSerializer, InteraccionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UsuarioSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class InteraccionViewSet(viewsets.ModelViewSet):
    queryset = Interaccion.objects.all()
    serializer_class = InteraccionSerializer
    
class RegistroUsuarioView(APIView):
    permission_classes = [AllowAny]  # Permitir que cualquier usuario acceda a esta vista

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=serializer.validated_data['email']).exists():
                return Response({"error": "Este correo electrónico ya está registrado."}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(username=serializer.validated_data['username']).exists():
                return Response({"error": "Este nombre de usuario ya está registrado."}, status=status.HTTP_400_BAD_REQUEST)

            User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                email=serializer.validated_data['email']
            )
            return Response({"mensaje": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username_or_email = attrs.get("username")
        password = attrs.get("password")

        user = User.objects.filter(username=username_or_email).first() or User.objects.filter(email=username_or_email).first()

        if user and user.check_password(password):
            attrs["username"] = user.username
        else:
            raise serializers.ValidationError("Credenciales inválidas.")

        return super().validate(attrs)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer