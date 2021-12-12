from django.http import HttpResponse
import datetime
def saludo(request):
	return HttpResponse("hola django YEAH")

def chau(request):
    return HttpResponse("Lorem Ipsum <br><br> hoes on my dick cause i look like fanta :D")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)