from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from GestionPedidos.forms import FormularioContacto

# Create your views here.
def Busqueda_productos(request):
    return render(request,'busqueda_productos.html')

def Buscar(request):
    if request.GET['prd']:
        #mensaje = 'Articulo :%r'%request.GET['prd']
        producto = request.GET['prd']
        if len(producto) > 20:
            mensaje = 'Texto Demaciado Grande'
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, 'resultado_busqueda.html',{'articulos':articulos,'query':producto})
    else:
        mensaje = 'No hay dato'
    
    return HttpResponse(mensaje)


#def contacto(request):
    if request.method=="POST":
        subject = request.POST['Asunto']
        messege = request.POST['Mensaje'] + ' ' +  request.POST['Email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['wieneber76@gmail.com']
        send_mail(subject,messege,email_from ,recipient_list)

        return render(request,"gracias.html")
    return render(request,"contacto.html")

def contacto(request):
    miFormulario = FormularioContacto(request.POST)
    if request.method == "POST":
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            info= miFormulario.cleaned_data
            send_mail(info['asunto'],info['mensaje'],info.get('email',''),["wieneber76@gmail.com"])
            return render(request , "gracias.html")
    else:
        miFormulario = FormularioContacto()
    return render(request, "formulario_contacto.html",{"form":miFormulario})
    