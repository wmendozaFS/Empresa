# EmpresaGestion/urls.py

"""
Definición de URL para el proyecto EmpresaGestion.

La lista `urlpatterns` enruta las URL a las vistas. Para obtener más información, consulte:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Ejemplos:
Función de vista
    1. Agrega una importación: from my_app import views
    2. Agrega una URL a urlpatterns: path('ruta/', views.home, name='home')
Vista basada en clases
    1. Agrega una importación: from other_app.views import Home
    2. Agrega una URL a urlpatterns: path('ruta/', Home.as_view(), name='home')
Incluyendo otra configuración de URL
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una URL a urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gestion_empresa.urls')), # Incluye las URLs de tu aplicación gestion_empresa
]