from django import forms 

class AlumnosForm(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    apellido=forms.CharField(max_length=50, required=True)
    edad=forms.IntegerField(required=True)
    tutor=forms.CharField(max_length=50, required=True)
    
class MaestrasForm(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    apellido=forms.CharField(max_length=50, required=True)
    edad=forms.IntegerField(required=True)
    email=forms.EmailField(required=True)


class EventosForm(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    fecha=forms.DateField(required=True)
        