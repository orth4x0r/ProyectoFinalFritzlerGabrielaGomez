from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.template import Context, Template, loader
import datetime

from AppCoderProyecto.models import Curso
# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarollo de alfajores", camada="69")
    curso.save()
    documentoDeTexto =f"------>Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

