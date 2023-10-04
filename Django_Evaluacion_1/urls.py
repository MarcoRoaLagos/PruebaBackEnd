"""
URL configuration for Django_Evaluacion_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from productos_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('juegos/',views.juegos),
    path('figuras/',views.figuras),
    path('juegosmesa/',views.juegosmesa),
    path('usuario/',views.usuario),
    path("juegos/mk1/",views.mk1),
    path('juegos/ratchet&clank/',views.ratchet),
    path('juegos/spiderman2/',views.spiderman2),
    path('juegos/gow/',views.gow),
    path('figuras/ashe/',views.ashe),
    path('figuras/alien/',views.alien),
    path('figuras/genio/',views.genio),
    path('figuras/skeletor/',views.skeletor),
    path('juegosmesa/catan/',views.catan),
    path('juegosmesa/kittens/',views.kittens),
    path('juegosmesa/dixit/',views.dixit),
    path('juegosmesa/burrito/',views.burrito)
]
