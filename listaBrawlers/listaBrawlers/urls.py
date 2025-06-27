"""
URL configuration for listaBrawlers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.listaMusicas, name='listaMusicas'),
    path('admin/', admin.site.urls),
    path('musica/<int:pk>/', views.detalheMusica, name='detalheMusica'),
]
admin.site.site_header = "Meu Painel de Musicas"
admin.site.site_title = "Admin Musicas"
admin.site.index_title = "Gerenciamento de Musicas"


if settings.DEBUG:
    #esse negocio é pra se tiver no modo com debug ele vai pegar os static 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

