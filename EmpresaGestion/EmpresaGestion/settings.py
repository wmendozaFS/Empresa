# EmpresaGestion/settings.py

"""
Configuración de Django para el proyecto EmpresaGestion.

Para obtener más información sobre este archivo, consulte
https://docs.djangoproject.com/en/5.0/topics/settings/

Para ver la lista completa de configuraciones y sus valores predeterminados, consulte
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from decouple import config
from pathlib import Path
from django.conf.global_settings import INTERNAL_IPS

# Construye rutas dentro del proyecto como: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración de seguridad
# ¡ADVERTENCIA DE SEGURIDAD: mantenga la clave secreta utilizada en producción en secreto!
SECRET_KEY = config('SECRET_KEY')

# ¡ADVERTENCIA DE SEGURIDAD: no ejecute con DEBUG = True en producción!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=list)


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
    'tailwind',  # Añade Tailwind CSS
    'django_browser_reload',  # Añade Django Browser Reload para recarga automática
    'theme',  # Nombre de la aplicación de Tailwind CSS
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
        'DIRS': [BASE_DIR / 'templates'],
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

if config('DB_ENGINE', default='mysql') == 'mysql': # Verifica el motor de la base de datos
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": config('DB_NAME'),
            "USER": config('DB_USER'),
            "PASSWORD": config('DB_PASSWORD'),
            "HOST": config('DB_HOST'),
            "PORT": config('DB_PORT')
        }
    }
elif config('DB_ENGINE', default='mysql') == 'sqlite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',  # Base de datos SQLite en el directorio del proyecto
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

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Directorio para archivos subidos por el

# Tipo de campo de clave primaria predeterminado
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TAILWIND_APP_NAME = 'theme'  # Nombre de la aplicación de Tailwind CSS

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]
#npm
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"  # Ruta al ejecutable de npm, ajusta según tu instalación

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
