from django.shortcuts import render
from django.http import HttpResponse
from.models import Curso
# Create your views here.

def homepage(request):
    return render (request,"main/inicio.html/", {"cursos": Curso.objects.all})
    return HttpResponse("Hola estudiantes del instituto Juan Montalvo, es un honor tenerlos nuevamente en las instalaciones de la institució.")
