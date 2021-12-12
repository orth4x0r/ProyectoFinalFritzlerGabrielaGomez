from django import template
from django.http import HttpResponse
from django.template import Context, Template
import datetime

def saludo(request):
	return HttpResponse("hola django YEAH")

def chau(request):
    return HttpResponse("Lorem Ipsum <br><br> hoes on my dick cause i look like fanta :D")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es:<br><br> {nombre}"

    return HttpResponse(documentoDeTexto)

def testTemplate(self):
    miHtml = open("C:\Users\ilanf\Desktop\CODERHOUSE\ProyectoFinal\ProyectoFinalFritzlerGabrielaGomez\ProyectoDjango\ProjectoFinal\ProjectoFinal\plantillas\template1.html")

    plantilla = Template(miHtml.read()) #carga en mem doc, template1

    miHtml.close()

    miContexto = Context()
    
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

