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
from DISClib.ADT import list as lt
assert cf


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


def requerimiento1(catalog, ciudad):
    info= controller.requerimiento1(catalog, ciudad)
    print('El total de avistamientos: ' + str(lt.size(info)))
    for i in range(1,4):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        print(fecha + '  '+ ciudad1 + '  ' + pais+'  '+ segs + '  '+ forma)
    for i in range(lt.size(info) -2, lt.size(info)+1):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        print(fecha + '  '+ ciudad1 + '  ' + pais+'  '+ segs + '  '+ forma)
    

def requerimiento2(tiempo_min, tiempo_max):
    info= controller.requerimiento2(catalog, tiempo_min, tiempo_max)
    print('El total de avistamientos: ' + str(lt.size(info)))
    for i in range(1,4):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        print(fecha + '  '+ ciudad1 + '  ' + pais+'  '+ segs + '  '+ forma)
    for i in range(lt.size(info) -2, lt.size(info)+1):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        print(fecha + '  '+ ciudad1 + '  ' + pais+'  '+ segs + '  '+ forma)


def requerimiento3(hora_min, hora_max):
    info=controller.requerimiento3(catalog, hora_min, hora_max)
    print('El total de avistamientos: ' + str(lt.size(info)))
    for i in range(1,4):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        print(fecha + '  '+ ciudad1 + '  ' + pais+'  '+ segs + '  '+ forma)
    for i in range(lt.size(info) -2, lt.size(info)+1):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        print(fecha + '  '+ ciudad1 + '  ' + pais+'  '+ segs + '  '+ forma)

def requerimiento4(catalog, tiempo_año_1, tiempo_año_2):
    info= controller.requerimiento4(catalog, tiempo_año_1, tiempo_año_2)
    print('El total de avistamientos: ' + str(lt.size(info)))
    for i in range(1,4):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        print(fecha + '  '+ ciudad1 + '  ' + pais+'  '+ segs + '  '+ forma)
    for i in range(lt.size(info) -2, lt.size(info)+1):
        fecha= lt.getElement(info, i)['datetime']
        ciudad1= lt.getElement(info, i)['city']
        pais= lt.getElement(info, i)['country']
        segs= lt.getElement(info, i)['duration (seconds)']
        forma= lt.getElement(info, i)['shape']
        print(fecha + '  '+ ciudad1 + '  ' + pais+'  '+ segs + '  '+ forma)


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
        print5(info)

    elif int(inputs[0]) == 2:
        ciudad= input('Ingrese la ciudad a consultar: ')
        requerimiento1(catalog, ciudad)
    
    elif int(inputs[0]) == 3:
        tiempo_min= input('Ingrese tiempo minimo: ')
        tiempo_max= input('Ingrese tiempo maximo: ')
        requerimiento2(tiempo_min, tiempo_max)
    
    elif int(inputs[0]) == 4:
        hora1= input('Ingrese hora minimo: ')
        hora2= input('Ingrese hora maximo: ')
        requerimiento3(hora1,hora2)

    elif int(inputs[0]) == 5:
        hora1= input('Ingrese año 1: ')
        hora2= input('Ingrese año 2: ')
        requerimiento4(hora1,hora2)
    else:
        sys.exit(0)
sys.exit(0)
