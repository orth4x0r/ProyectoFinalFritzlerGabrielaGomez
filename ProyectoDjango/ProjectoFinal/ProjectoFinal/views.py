from django import template
from django.http import HttpResponse
from django.template import Context, Template, loader
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

    #miHtml = open(r"C:\Users\ilanf\Desktop\CODERHOUSE\ProyectoFinal\ProyectoFinalFritzlerGabrielaGomez\ProyectoDjango\ProjectoFinal\ProjectoFinal\plantillas\template1.html")

    nom = "Ilan"
    ap = "Fritzler"
    fechaAhora = datetime.datetime.now()

    diccionario = {"nombre":nom, "apellido":ap, "fecha":fechaAhora}

    #plantilla = Template(miHtml.read()) #carga en mem doc, template1
    plantilla = loader.get_template('template1.html')
    #miHtml.close()

    #miContexto = Context(diccionario)
    
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

