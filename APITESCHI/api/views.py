from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

#librerias para iniciar el login
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


class home (APIView):
    template_name="index.html"
    def get (self, resquest):
        return render(resquest, self.template_name)
class inicio (APIView):
    template_name="inicio.html"
    def get (self, resquest):
        return render(resquest,self.template_name )
    
    def post(self, request):
        user=authenticate(request, username=request.POST['correo'], password=request.POST['password'])
        if user is None:
              return render(request,self.template_name, {"error":"Contraseña o Usuario incorrecto"})
        else: 
            login(request,user) 
            return redirect ('inicio')
        
class Crear_usuario(APIView):
    template_name="CrearUsuario.html"
    def get(self, request):
        return render(request, self.template_name, {
            "formulario": UserCreationForm
        })
    def post(self, request):
        if request.user.is_aunthenticated:
            try:
               user = User.objects.create_user(
                   username= request.POST[""],
                   password= request.POST[""]
               )
               user.save()
               return redirect ('inicio') 
            except IntegrityError:
                 return render(request, self.template_name, {
                  "formulario": UserCreationForm,
                  "error": "Error al cargar el formulario"
                  })
        

        
            