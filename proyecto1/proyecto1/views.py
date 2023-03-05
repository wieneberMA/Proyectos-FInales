from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template.loader import get_template
from django.shortcuts import render

def saludo(request): # primer vista que nos permite la primera respuesta
    nombre = "Proverbio etíope."
    nombre2 = "Hellen Keller."
    TemasDelCurso = ["Plantillas","Modelos","Formularios","Vistas","Despliegueapp"]
    #doc_externo = open("C:/Users/wieneber/Desktop/proyectosDjango/proyecto1/proyecto1/plantillas/plantilladepoema.html")
    #ptl = Template(doc_externo.read())
    #doc_externo.close()
    #doc = get_template("plantilladepoema.html")
    #ctx = Context({"nombre_persona":nombre,"nombre_persona2":nombre2,"Tema":TemasDelCurso})
    #documento = doc.render({"nombre_persona":nombre,"nombre_persona2":nombre2,"Tema":TemasDelCurso})
    return render(request, "plantilladepoema.html",{"nombre_persona":nombre,"nombre_persona2":nombre2,"Tema":TemasDelCurso})


def despedida(request):
    return HttpResponse("hasta luego maricarmen")

def frace(request):
    texto = """Mantener un alto nivel de motivación en el clima laboral es una tarea difícil. No todos los días uno consigue resolver los problemas que se le plantean;
    surgen dudas, inseguridades, se desencadenan conflictos con otros compañeros. Un buen líder siempre tiene que estar en el momento justo para levantar los ánimos y encontrar la manera
     de desenmarañar los momentos de bloqueo y hacer que sus compañeros vean la luz al final del túnel."""
    return HttpResponse(texto)

def hora(request):
    fecha = datetime.datetime.now()
    texto = "Ninguno de nosotros es tan bueno como todos nosotros juntos. Ray Kroc. %s" %fecha
    return HttpResponse(texto)

def calculaedad(request,edad,agno):
    periodo = agno - 2022
    edadfutura = edad+periodo
    texto = "el anio %s tendras %s anios"%(agno,edadfutura)
    return HttpResponse(texto)

def cursodjango(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"cursoc.html",{"fecha":fecha_actual})
