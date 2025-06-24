"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [

        path('', views.indexBarrio, name='barrioIndex'),
        path('barrios/<int:id>', views.barrios, name='barrios'),
        path('crear/barrio', views.crearBarrio,name='crearbarrio'),   
        path('crear/parroquia', views.crearParroquia,name='crearparroquia'), 
 ]
