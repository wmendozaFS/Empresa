# EmpresaGestion/settings.py

"""
Configuración de Django para el proyecto EmpresaGestion.

Para obtener más información sobre este archivo, consulte
https://docs.djangoproject.com/en/5.0/topics/settings/

Para ver la lista completa de configuraciones y sus valores predeterminados, consulte
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Construye rutas dentro del proyecto como: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración de seguridad
# ¡ADVERTENCIA DE SEGURIDAD: mantenga la clave secreta utilizada en producción en secreto!
SECRET_KEY = 'django-insecure-your-secret-key-here-please-change-this' # ¡Cambia esta clave en producción!

# ¡ADVERTENCIA DE SEGURIDAD: no ejecute con DEBUG = True en producción!
DEBUG = True

ALLOWED_HOSTS = []


# Definición de aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Añade Django REST Framework
    'gestion_empresa', # Añade tu aplicación
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EmpresaGestion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EmpresaGestion.wsgi.application'


# Base de datos
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Opciones: 'sqlite3', 'postgresql', 'mysql', 'oracle'
        'NAME': 'Empresa',                    # Nombre de tu base de datos
        'USER': 'root',                       # Tu usuario de base de datos
        'PASSWORD': 'your_mysql_password',    # Tu contraseña de base de datos (¡Cámbiala!)
        'HOST': 'localhost',                  # O la IP de tu servidor de base de datos
        'PORT': '3306',                       # Puerto de MySQL
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


# Validadores de contraseña
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalización
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-es' # Establece el idioma a español

TIME_ZONE = 'Europe/Madrid' # Ajusta la zona horaria a España

USE_I18N = True

USE_TZ = True


# Archivos estáticos (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Tipo de campo de clave primaria predeterminado
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny' # Permite acceso sin autenticación para este ejemplo.
                                             # Para producción, deberías usar 'IsAuthenticated', etc.
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer', # Útil para depuración en el navegador
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10 # Número de elementos por página en las respuestas de la API
}
