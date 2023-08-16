from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('historia/', historia, name="historia"),
    path('salas/', salas, name="salas"),
    path('alumnos/', alumnos, name="alumnos"),
    path('maestras/', maestras, name="maestras"),
    path('eventos/', eventos, name="eventos"),

    path('alumnos_form/', alumnosForm, name="alumnos_form"),
    path('alumnos_form2/', alumnosForm2, name="alumnos_form2"),
    path('maestras_form/', maestrasForm, name="maestras_form"),
    path('eventos_form/', eventosForm, name="eventos_form"),
    
    path('buscar_alumno/', buscarAlumno, name="buscar_alumno"),
    path('buscar_alumno2/', buscarAlumno2, name="buscar_alumno2"),
    
    
  
]