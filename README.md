# Asistente Virtual Avanzado 

**Descripción**: Este proyecto sera un asistente virtual avanzado que permite a los usuarios interactuar mediante comandos de voz y texto, con autenticación, visualización de usuarios y otras funcionalidades. Se compone de un backend en Django (con Django REST Framework) y un frontend en Flutter.

---

## Estructura del Proyecto

### 1. Frontend - Flutter

El frontend permite a los usuarios iniciar sesión, registrarse y ver una lista de usuarios registrados. Utiliza `ApiService` para manejar las peticiones al backend.

#### Archivos Principales

- **api\_service.dart**: Gestiona las solicitudes HTTP hacia el backend. Incluye métodos para:

  - `login()`: Iniciar sesión y almacenar el token de acceso.
  - `getUsuarios()`: Obtener la lista de usuarios autenticados.
  - `registrarUsuario()`: Registrar un nuevo usuario.

- **registro\_screen.dart**: Pantalla para el registro de usuario, con validación y manejo de errores.

- **main.dart**: Punto de entrada de la aplicación. Incluye la navegación entre pantallas de inicio de sesión, registro y visualización de usuarios.

### 2. Backend - Django

El backend gestiona las operaciones de usuario e interacción, proporcionando autenticación mediante JWT (JSON Web Tokens) y CRUD para usuarios e interacciones.

#### Archivos Principales

- **models.py**: Define los modelos `Usuario` e `Interaccion` para almacenar datos de usuarios e interacciones.
- **serializers.py**: Contiene los serializadores para los modelos, que convierten los datos a JSON para su transmisión a través de la API.
- **views.py**: Define las vistas basadas en clases y APIView para manejar el registro de usuarios, autenticación y CRUD de interacciones.
- **urls.py**: Configura las rutas del backend, incluyendo `/api/token/` para autenticación y `/api/registro/` para registro de usuarios.
- **settings.py**: Configuración principal del proyecto, incluyendo ajustes de base de datos, JWT y CORS.

---

## Configuración del Proyecto

### Requisitos Previos

- **Python 3.x** y **Django**: Para ejecutar el backend.
- **Flutter**: Para ejecutar el frontend.
- **PostgreSQL**: Base de datos utilizada para almacenar datos de usuarios e interacciones.

### Configuración del Backend (Django)

1. **Clonar el Proyecto**:

   ```bash
   git clone https://github.com/Jeremitc/FlutterProject.git
   cd FlutterProject/Backend/asistente_virtual
   ```

2. **Instalar Dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar la Base de Datos**:

   - Asegúrate de tener una base de datos PostgreSQL configurada y de actualizar `settings.py` con tus credenciales.

4. **Migrar la Base de Datos**:

   ```bash
   python manage.py migrate
   ```

5. **Ejecutar el Servidor**:

   ```bash
   python manage.py runserver
   ```

### Configuración del Frontend (Flutter)

1. **Navegar al Directorio del Proyecto Flutter**:

   ```bash
   cd ../Frontend/asistente_virtual_app
   ```

2. **Instalar Dependencias**:

   ```bash
   flutter pub get
   ```

3. **Ejecutar la Aplicación**:

   - Conecta un emulador o dispositivo y ejecuta:
     ```bash
     flutter run
     ```

---

## Uso de la Aplicación

1. **Inicio de Sesión**: Los usuarios pueden iniciar sesión usando su nombre de usuario o correo electrónico. Se utiliza JWT para autenticación.
2. **Registro de Usuario**: La aplicación permite registrar nuevos usuarios, guardando la información en la base de datos de Django.
3. **Visualización de Usuarios**: Tras iniciar sesión, se muestra una lista de usuarios registrados en el sistema.

---

## Archivos Clave

### requirements.txt

Lista de dependencias para el backend en Django:

```plaintext
asgiref==3.8.1
Django==5.1.3
django-cors-headers==4.6.0
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
psycopg==3.2.3
psycopg2-binary==2.9.10
PyJWT==2.9.0
sqlparse==0.5.1
tzdata==2024.2
```

### Configuración de JWT en `settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

### API Endpoints en `urls.py`

- **Autenticación JWT**:
  - `/api/token/`: Obtener el token de acceso.
  - `/api/token/refresh/`: Refrescar el token de acceso.
- **Registro de Usuario**:
  - `/api/registro/`: Crear un nuevo usuario.
- **Gestión de Usuarios e Interacciones**:
  - `/api/usuarios/`: Lista y detalles de usuarios.
  - `/api/interacciones/`: CRUD de interacciones.

#### Estructura de `serializers.py`

```python
from rest_framework import serializers
from .models import Usuario, Interaccion
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Campos para el registro de usuario
        extra_kwargs = {
            'password': {'write_only': True}
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
```

#### Vistas Clave en `views.py`

- **UsuarioViewSet**: Gestión de usuarios autenticados.
- **InteraccionViewSet**: CRUD de interacciones del asistente.
- **RegistroUsuarioView**: Vista para registrar usuarios.
- **CustomTokenObtainPairView**: Autenticación personalizada que permite iniciar sesión con nombre de usuario o correo electrónico.

---

## Contribuciones

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios (`git checkout -b feature/nueva-funcion`).
3. Realiza commit de tus cambios (`git commit -m 'Añadir nueva función'`).
4. Haz push a tu rama (`git push origin feature/nueva-funcion`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## Contacto

Para más información, puedes contactar al propietario del proyecto a través de GitHub.

