from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    return render(request,"aplicacion/home.html")

def historia(request):
    
    return render(request,"aplicacion/historia.html")

def salas(request):
    contexto = {'salas': Sala.objects.all(), 'titulo': 'Salas'}
    return render(request,"aplicacion/salas.html", contexto)

def alumnos(request):
    contexto = {'alumnos': Alumnos.objects.all(), 'titulo': 'Listado de Alumnos'}
    return render(request,"aplicacion/alumnos.html", contexto)

    

def maestras(request):
    contexto = {'maestras': Maestras.objects.all(), 'titulo': 'Listado de Maestras'}
    return render(request,"aplicacion/maestras.html", contexto)

def eventos(request):
    contexto = {'eventos': Eventos.objects.all(), 'titulo': 'Eventos'}
    return render(request,"aplicacion/eventos.html", contexto)

def alumnosForm(request):
    if request.method == "POST":   
        alumno = Alumnos(nombre=request.POST['nombre'],
                         apellido=request.POST['apellido'],
                         edad=request.POST['edad'],
                         tutor=request.POST['tutor'])
        alumno.save()

        return HttpResponse("Se grabó el registro")
    
    return render(request,"aplicacion/alumnosForm.html")


def alumnosForm2(request):
    if request.method == "POST":   
        miForm = AlumnosForm(request.POST)
        
        if miForm.is_valid():
            alumno_nombre = miForm.cleaned_data.get('nombre')
            alumno_apellido = miForm.cleaned_data.get('apellido')
            alumno_edad = miForm.cleaned_data.get('edad')
            alumno_tutor = miForm.cleaned_data.get('tutor')
            alumno = Alumnos(nombre=alumno_nombre, 
                             apellido=alumno_apellido, 
                             tutor=alumno_tutor, 
                             edad=alumno_edad)
            alumno.save()

            return render(request, "aplicacion/base.html")
   
    else:
        miForm = AlumnosForm()

    return render(request, "aplicacion/alumnosForm2.html", {"form":miForm})


def maestrasForm(request):
    if request.method == "POST":   
        miForm = MaestrasForm(request.POST)
        
        if miForm.is_valid():
            maestra_nombre = miForm.cleaned_data.get('nombre')
            maestra_apellido = miForm.cleaned_data.get('apellido')
            maestra_email = miForm.cleaned_data.get('email')
            maestra_edad = miForm.cleaned_data.get('edad')
            maestra = Maestras(nombre=maestra_nombre, 
                             apellido=maestra_apellido, 
                             email=maestra_email, 
                             edad=maestra_edad)
            maestra.save()

            return render(request, "aplicacion/base.html")
   
    else:
        miForm = MaestrasForm()

    return render(request, "aplicacion/maestrasForm.html", {"form":miForm})


def eventosForm(request):
    if request.method == "POST":   
        miForm = EventosForm(request.POST)
        
        if miForm.is_valid():
            evento_nombre = miForm.cleaned_data.get('nombre')
            evento_fecha = miForm.cleaned_data.get('fecha')
            evento = Eventos(nombre=evento_nombre, 
                             fecha=evento_fecha) 
                             
            evento.save()

            return render(request, "aplicacion/base.html")
   
    else:
        miForm = EventosForm()

    return render(request, "aplicacion/eventosForm.html", {"form":miForm})



def buscarAlumno(request):
    return render(request, "aplicacion/buscaralumno.html")

def buscarAlumno2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        alumnos = Alumnos.objects.filter(nombre__icontains=patron)
        contexto= {"alumnos": alumnos, 'titulo':f'Alumnos tiene como patron "{patron}"'}
             
        return render(request, "aplicacion/alumnos.html", contexto) 
    return HttpResponse("No se ingresaron datos para buscar!")