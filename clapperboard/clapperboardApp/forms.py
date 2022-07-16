from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña",  widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'] 
        # help_texts= {k:"" for k in fields}
               
class UserEditForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    email= forms.EmailField(label="Email")
    password1: forms.CharField(label="Contraseña",  widget=forms.PasswordInput, required=False)
    password2: forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    
    class Meta:
        model = User
        fields= ['first_name', 'last_name', 'email', 'password1', 'password2']
        
class AvatarForm(forms.Form):
     
    imagen = forms.ImageField(label="Imagen")
    
    class Meta:
        model = Avatar
        fields = ['imagen']

class nueva_pelicula(forms.Form):
    titulo = forms.CharField(label="Titulo")
    descripcion = forms.CharField(label="Descripcion")
    imagen = forms.ImageField(label="Imagen")
    fecha_publicacion = forms.DateField(label="Fecha de publicacion")
    usuario = forms.CharField(label="Usuario")
    
    class Meta:
        model = Pelicula
        fields = ['titulo', 'descripcion', 'imagen', 'fecha_publicacion', 'usuario']

class nueva_serie(forms.Form):
    titulo = forms.CharField(label="Titulo")
    descripcion = forms.CharField(label="Descripcion")
    imagen = forms.ImageField(label="Imagen")
    fecha_publicacion = forms.DateField(label="Fecha de publicacion")
    usuario = forms.CharField(label="Usuario")
    
    class Meta:
        model = Series
        fields = ['titulo', 'descripcion', 'imagen', 'fecha_publicacion', 'usuario']

class nuevo_juego(forms.Form):
    titulo = forms.CharField(label="Titulo")
    descripcion = forms.CharField(label="Descripcion")
    imagen = forms.ImageField(label="Imagen")
    fecha_publicacion = forms.DateField(label="Fecha de publicacion")
    usuario = forms.CharField(label="Usuario")
    
    class Meta:
        model = Juegos
        fields = ['titulo', 'descripcion', 'imagen', 'fecha_publicacion', 'usuario']

class nueva_musica(forms.Form):
    titulo = forms.CharField(label="Titulo")
    descripcion = forms.CharField(label="Descripcion")
    imagen = forms.ImageField(label="Imagen")
    fecha_publicacion = forms.DateField(label="Fecha de publicacion")
    usuario = forms.CharField(label="Usuario")
    
    class Meta:
        model = Musica
        fields = ['titulo', 'descripcion', 'imagen', 'fecha_publicacion', 'usuario']

class nuevo_comentario(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=300, required=True, widget=forms.Textarea)

        