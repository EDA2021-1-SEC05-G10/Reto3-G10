"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import time
from DISClib.ADT import list as lt
assert cf
from prettytable import PrettyTable
from DISClib.DataStructures import orderedmapstructure as om
from DISClib.DataStructures import mapentry as me
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Requerimiento 1")
    print("3- Requerimiento 2")
    print("4- Requerimiento 3")
    print("5- Requerimiento 4")
    print("6- Requerimiento 5")
    print("7- Bono")
    print("0- Salir")

catalog = None
def print5(info):
    tabla = PrettyTable()
    tabla.field_names = ["Datetime","City","Country","Duration (seconds)","Shape"]
    for i in range(1,6):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        datos = [fecha,ciudad1,pais,segs,forma]
        tabla.add_row(datos)
    for i in range(lt.size(info) -4, lt.size(info)+1):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        datos = [fecha,ciudad1,pais,segs,forma]
        tabla.add_row(datos)
    return tabla

def requerimiento1(catalog, ciudad):
    datos = controller.requerimiento1(catalog,ciudad)
    tabla = PrettyTable()
    tabla.field_names = ["Date", "City","State","Country" ,"Shape","Duration (seconds)"]  
    tabla._max_width={"Date":20,"City":20, "State":20, "Country":20,"Shape":20 ,"Duration (seconds)":20,}  
    i = 0
    for cada in lt.iterator(datos):
        if int(i) < 3 or int(i) >=int(lt.size(datos))-3:
            x = [cada["datetime"],cada["city"],cada["state"],cada["country"],cada["shape"],cada["duration (seconds)"]]
            tabla.add_row(x)
        i+=1
    return tabla.get_string(sortby="Date")
    

def requerimiento2(tiempo_min, tiempo_max):
    inicio=time.time()
    info= controller.requerimiento2(catalog, tiempo_min, tiempo_max)
    tabla = PrettyTable()
    tabla.field_names = ["Datetime","City","Country","Duration (seconds)","Shape"]
    print('El total de avistamientos: ' + str(lt.size(info)))
    i=0

    for cada in lt.iterator(info):
        for cada2 in lt.iterator(cada):
            if i<3 or i>lt.size(info)-3:
                x = [cada2["datetime"],cada2["city"],cada2["country"],cada2["duration (seconds)"],cada2["shape"]]
                tabla.add_row(x)
            i+=1

    fin=time.time()
    print(fin-inicio)
    return tabla

def requerimiento3(catalog, minimo, maximo):
    maxHor, cant, datos = controller.requerimiento3(catalog, minimo, maximo)
    tabla = PrettyTable()
    tabla.field_names = ["Time", "Count",]
    dat = [maxHor,cant]
    tabla.add_row(dat)

    tabla2 = PrettyTable()
    tabla2.field_names = ["Datetime","City","State","Country" ,"Shape","Duration (seconds)"]
    max = om.maxKey(datos)
    min = om.minKey(datos)
    size = lt.size(me.getValue(om.get(datos,max)))
    i=0
    j=0
    for cada in lt.iterator(me.getValue(om.get(datos,min))):
        if j < 3:
            x = [cada["datetime"],cada["city"],cada["state"],cada["country"],cada["shape"],cada["duration (seconds)"]]
            tabla2.add_row(x)
        j+=1
    for cada in lt.iterator(me.getValue(om.get(datos,max))):
        if i >=size-3:
            x = [cada["datetime"],cada["city"],cada["state"],cada["country"],cada["shape"],cada["duration (seconds)"]]
            tabla2.add_row(x)
        i+=1
    
    return tabla, tabla2

def requerimiento4(tiempo_año_1, tiempo_año_2):
    inicio=time.time()
    info= controller.requerimiento4(catalog, tiempo_año_1, tiempo_año_2)
    tabla = PrettyTable()
    tabla.field_names = ["Datetime","City","Country","Duration (seconds)","Shape"]
    print('El total de avistamientos: ' + str(lt.size(info)))
    for i in range(1,4):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        datos = [fecha,ciudad1,pais,segs,forma]
        tabla.add_row(datos)
    for i in range(lt.size(info) -2, lt.size(info)+1):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        datos = [fecha,ciudad1,pais,segs,forma]
        tabla.add_row(datos)
    fin=time.time()
    return tabla,(fin-inicio)
    

def requerimiento5(catalog,lonMin,lonMax,latMin,latMax):
    datos = controller.requerimiento5(catalog,lonMin,lonMax,latMin,latMax)
    tabla = PrettyTable()
    tabla.field_names = ["Datetime","City","State","Country" ,"Shape","Duration (seconds)","Latitude","Longitude"]
    tabla._max_width={"Datetime":20,"City":17,"State":5,"Country":10 ,"Shape":15,"Duration (seconds)":15,"Latitude":15,"Longitude":15}
    i = 0
    for cada in lt.iterator(datos):
        if i < 5 or i >lt.size(datos)-5:
            x = [cada["datetime"],cada["city"],cada["state"],cada["country"],cada["shape"],cada["duration (seconds)"],round(float(cada["latitude"]),2),round(float(cada["longitude"]),2)]
            tabla.add_row(x)
    return tabla 


def bono(longitud_max, longitud_min, latitud_min, latitud_max):
    inicio=time.time()
    info= controller.bono(catalog, float(longitud_max), float(longitud_min), float(latitud_min), float(latitud_max))
    print('El total de avistamientos: ' + str(lt.size(info)))
    for i in range(1,6):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        print(fecha + '  '+ ciudad1 + '  ' + pais+'  '+ segs + '  '+ forma)
    for i in range(lt.size(info) -4, lt.size(info)+1):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        print(fecha + '  '+ ciudad1 + '  ' + pais+'  '+ segs + '  '+ forma)
    fin=time.time()
    print(fin-inicio)

"""
 
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog= controller.initCatalog()
        info= controller.loadData(catalog)
        print(print5(info))

    elif int(inputs[0]) == 2:
        ciudad= input('Ingrese la ciudad a consultar: ')
        print(requerimiento1(catalog, ciudad))
    
    elif int(inputs[0]) == 3:
        tiempo_min= input('Ingrese tiempo minimo: ')
        tiempo_max= input('Ingrese tiempo maximo: ')
        print(requerimiento2(tiempo_min, tiempo_max))
        

    elif int(inputs[0]) == 4:
        minimo= input('Ingrese hora minimo: ')
        maximo= input('Ingrese hora maximo: ')
        tabla, tabla2 = requerimiento3(catalog,minimo,maximo)
        print(tabla)
        print(tabla2)

    elif int(inputs[0]) == 5:
        Año1= input('Ingrese año 1(AAAA-MM-DD): ')
        Año2= input('Ingrese año 2(AAAA-MM-DD): ')
        tabla,tiempo =requerimiento4(Año1, Año2)
        print(tabla,tiempo)
    
    elif int(inputs[0]) == 6:
        lonMin = input("Ingrese longitud mínima: ")
        lonMax = input("Ingrese longitud máxima: ")
        latMin = input("Ingrese latitud mínima: ")
        latMax = input("Ingrese latitud máxima: ")
        print(requerimiento5(catalog,lonMin,lonMax,latMin,latMax))

    elif int(inputs[0]) == 7:
        longitud1= input('Ingrese longitud-min: ')
        longitud2= input('Ingrese longitud-max: ')
        latitud1= input('Ingrese latitud-min: ')
        latitud2= input('Ingrese latitud-max: ')
        
        bono(longitud2, longitud1, latitud1, latitud2)
    else:
        sys.exit(0)
sys.exit(0)
