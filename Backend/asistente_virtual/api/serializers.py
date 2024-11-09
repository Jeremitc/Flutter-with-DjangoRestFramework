from rest_framework import serializers
from .models import Usuario, Interaccion
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Definir los campos que se utilizarán para el registro
        extra_kwargs = {
            'password': {'write_only': True}  # Evitar que la contraseña se lea
        }
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user

class InteraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaccion
        fields = '__all__'

