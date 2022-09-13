#from django.shortcuts import render
from django.http import HttpResponse
from MVT_familia.models import Familia
from django.template import loader

# Create your views here.

def familia(self):
    familiar1 = Familia(nombre = "Patricia", edad = 64, fecha_nac = "1957-12-3")
    familiar1.save()

    familiar2 = Familia(nombre = "Alfredo", edad = 63, fecha_nac = "1958-12-8")
    familiar2.save()

    familiar3 = Familia(nombre = "Florencia", edad = 38, fecha_nac = "1984-6-22")
    familiar3.save()

    diccionario = {
        "nombre1": familiar1.nombre, "edad1": familiar1.edad, "cumple1": familiar1.fecha_nac,
        "nombre2": familiar2.nombre, "edad2": familiar2.edad, "cumple2": familiar2.fecha_nac,
        "nombre3": familiar3.nombre, "edad3": familiar3.edad, "cumple3": familiar3.fecha_nac
        }
    
    plantilla = loader.get_template("familiar.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
