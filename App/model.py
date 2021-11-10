﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import orderedmapstructure as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from math import *
import DISClib.DataStructures.linkedlistiterator as it
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newcatalog():
    catalog= {'cities': None, 'years':None, 'duration (seconds)': None, 'Horas': None,'location':None }
    catalog['years']= om.newMap(omaptype='BST',comparefunction=compareDates)
    catalog['cities']= om.newMap(omaptype='BST',comparefunction=compareDates)
    catalog['duration (seconds)']= om.newMap(omaptype='BST',comparefunction=compareDates)
    catalog['horas']=om.newMap(omaptype='BST',comparefunction=compareDates)
    catalog['location']=om.newMap(omaptype='BST',comparefunction=compareDates)
    return catalog
# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos
def add_cities(infocities, catalog):
    info= om.get(catalog['cities'], infocities['city'])
    if info is None:
        years= lt.newList('SINGLE_LINKED')
        lt.addLast(years, infocities)
        om.put(catalog['cities'],infocities['city'],years)
    else:
        lt.addLast(info['value'],infocities)

def add_duration(infoduration, catalog):
    info= om.get(catalog['duration (seconds)'], infoduration['duration (seconds)'])
    if info is None:
        years= lt.newList('SINGLE_LINKED')
        lt.addLast(years, infoduration)
        om.put(catalog['duration (seconds)'],infoduration['duration (seconds)'],years)
    else:
        lt.addLast(info['value'],infoduration)

def add_duration_hours(infodurationhours, catalog):
    hora= infodurationhours['datetime'].split(' ')
    horafinal= hora[1]
    info= om.get(catalog['horas'],horafinal)
    if info is None:
        years= lt.newList('SINGLE_LINKED')
        lt.addLast(years, infodurationhours)
        om.put(catalog['horas'],horafinal, years)
    else:
        lt.addLast(info['value'],infodurationhours)

def add_years(infoyears, catalog):
    fecha= infoyears['datetime'].split(' ')
    fechafinal= fecha[0]
    info= om.get(catalog['years'], fechafinal)
    if info is None:
        years= lt.newList('SINGLE_LINKED')
        lt.addLast(years, infoyears)
        om.put(catalog['years'],fechafinal,years)
    else:
        lt.addLast(info['value'],infoyears)

def add_location(infolocation, catalog):
    llave= infolocation['longitude']+ ','+ infolocation['latitude']
    info= om.get(catalog['location'], llave)
    if info is None:
        locacion= lt.newList('SINGLE_LINKED')
        lt.addLast(locacion, infolocation)
        om.put(catalog['duration (seconds)'],llave,locacion)
    else:
        lt.addLast(info['value'],infolocation)
        

# Funciones de consulta

def requerimiento1(catalog, ciudad):
    info=om.get(catalog['cities'], ciudad)['value']
    lista= lt.newList()
    iterator1= it.newIterator(info)
    while it.hasNext(iterator1):
        elemento=it.next(iterator1)
        if lt.size(lista) != 0:
            i=1
            j=lt.size(lista)
            while i <= j:
                if elemento['datetime'] < lt.getElement(lista, i)['datetime']:
                    viejo= lt.getElement(lista, i)
                    lt.deleteElement(lista, i)
                    lt.insertElement(lista, elemento, i)
                    lt.insertElement(lista,viejo,i+1)
                    break
                elif i == j:
                    lt.insertElement(lista, elemento,i+1)
                i+=1
        else:
            lt.addLast(lista, elemento)
    return lista

def requerimiento2(catalog, tiempo_min, tiempo_max):
    llaves= om.keys(catalog['duration (seconds)'], tiempo_min, tiempo_max)
    lista= lt.newList()
    iterator1=it.newIterator(llaves)
    print(catalog['duration (seconds)'])
    while it.hasNext(iterator1):
        elemento= it.next(iterator1)
        info= om.get(catalog['duration (seconds)'], elemento)['value']
        iterator2= it.newIterator(info)
        while it.hasNext(iterator2):
            elemento2= it.next(iterator2)
            if lt.size(lista) != 0:
                i= 1
                j= lt.size(lista)
                while i <= j:
                    if elemento2['duration (seconds)'] > lt.getElement(lista, i)['duration (seconds)']:
                        viejo= lt.getElement(lista, i)
                        lt.deleteElement(lista, i)
                        lt.insertElement(lista, elemento2, i)
                        lt.insertElement(lista,viejo,i+1)
                    elif elemento2['duration (seconds)'] == lt.getElement(lista, i)['duration (seconds)'] and elemento2['city'] > lt.getElement(lista, i)['city']:
                        viejo= lt.getElement(lista, i)
                        lt.deleteElement(lista, i)
                        lt.insertElement(lista, elemento2, i)
                        lt.insertElement(lista,viejo,i+1)
                    elif i == j:
                        lt.insertElement(lista, elemento2,i+1)
                    i+=1
            else: 
                lt.addLast(lista, elemento2)
    return lista 

def requerimiento3(catalog, hora_min, hora_max):
    minima= hora_min + ':00'
    maxima= hora_max + ':00'
    llaves=om.keys(catalog['horas'], minima, maxima)
    lista= lt.newList('SINGLE_LINKED')
    iterator1= it.newIterator(llaves)
    while it.hasNext(iterator1):
        elemento=it.next(iterator1)
        info= om.get(catalog['horas'], elemento)['value']
        iterator2=it.newIterator(info)
        while it.hasNext(iterator2):
            elemento2= it.next(iterator2)
            if lt.size(lista) == 0:
                lt.addFirst(lista, elemento2)
            else:
                i= 0
                j= lt.size(lista)
                while i < j:
                    i+=1
                    if elemento2['datetime'] < lt.getElement(lista, i)['datetime']:
                        viejo= lt.getElement(lista, i)
                        lt.deleteElement(lista, i)
                        lt.insertElement(lista, elemento2, i)
                        lt.insertElement(lista,viejo,i+1)
                        break
                        
                    elif elemento2['datetime'] == lt.getElement(lista, i)['datetime'] :
                        viejo= lt.getElement(lista, i)
                        lt.deleteElement(lista, i)
                        lt.insertElement(lista, elemento2, i)
                        lt.insertElement(lista,viejo,i+1)
                        break
                    elif i == j:
                        lt.insertElement(lista, elemento2,i+1)
                        break
    return lista

def requerimiento4(catalog, tiempo_año_1, tiempo_año_2):
    año1= tiempo_año_1 
    año2= tiempo_año_2 
    llaves=om.keys(catalog['years'], año1, año2)
    lista= lt.newList('SINGLE_LINKED')
    iterator1= it.newIterator(llaves)
    while it.hasNext(iterator1):
        elemento=it.next(iterator1)
        info= om.get(catalog['years'], elemento)['value']
        iterator2=it.newIterator(info)
        while it.hasNext(iterator2):
            elemento2= it.next(iterator2)
            if lt.size(lista) == 0:
                lt.addFirst(lista, elemento2)
            else:
                i= 0
                j= lt.size(lista)
                while i < j:
                    i+=1
                    if elemento2['datetime'] < lt.getElement(lista, i)['datetime']:
                        viejo= lt.getElement(lista, i)
                        lt.deleteElement(lista, i)
                        lt.insertElement(lista, elemento2, i)
                        lt.insertElement(lista,viejo,i+1)
                        break
                    elif elemento2['datetime'] == lt.getElement(lista, i)['datetime'] :
                        viejo= lt.getElement(lista, i)
                        lt.deleteElement(lista, i)
                        lt.insertElement(lista, elemento2, i)
                        lt.insertElement(lista,viejo,i+1)
                        break
                    elif i == j:
                        lt.insertElement(lista, elemento2,i+1)
                        break
                    
    return lista


def bono(catalog, longitud_max, longitud_min, latitud_min, latitud_max):
    radio= haversine(longitud_min,  latitud_min, longitud_max, latitud_max)
    llaves=om.keySet(catalog['cities'])
    lista= lt.newList('SINGLE_LINKED')
    iterator1= it.newIterator(llaves)
    while it.hasNext(iterator1):
        elemento=it.next(iterator1)
        info= om.get(catalog['cities'], elemento)['value']
        iterator2=it.newIterator(info)
        while it.hasNext(iterator2):
            elemento2= it.next(iterator2)
            radioa=haversine(longitud_min,latitud_min,float(elemento2['longitude']), float(elemento2['latitude']) )
            radiob=haversine(float(elemento2['longitude']), float(elemento2['latitude']),longitud_max,latitud_max, )
            print(radio)
            print(radioa)
            print(radiob)
            if radioa <= radio and radiob <= radio:
                if lt.size(lista) == 0:
                    lt.addFirst(lista, elemento2)
                else:
                    i= 0
                    j= lt.size(lista)
                    while i < j:
                        i+=1
                        if elemento2['datetime'] < lt.getElement(lista, i)['datetime']:
                            viejo= lt.getElement(lista, i)
                            lt.deleteElement(lista, i)
                            lt.insertElement(lista, elemento2, i)
                            lt.insertElement(lista,viejo,i+1)
                            break
                        elif elemento2['datetime'] == lt.getElement(lista, i)['datetime'] :
                            viejo= lt.getElement(lista, i)
                            lt.deleteElement(lista, i)
                            lt.insertElement(lista, elemento2, i)
                            lt.insertElement(lista,viejo,i+1)
                            break
                        elif i == j:
                            lt.insertElement(lista, elemento2,i+1)
                            break      
    return lista

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    formula tomada de https://stackoverflow.com/questions/42686300/how-to-check-if-coordinate-inside-certain-area-python
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)*2 + cos(lat1) * cos(lat2) * sin(dlon/2)*2
    c = 2 * asin(sqrt(a)) 
    r = 3956 # Radius of earth in miles. Use 3956 for miles
    return c * r













# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareDates(Fecha1,Fecha2):
    if Fecha1 < (Fecha2):
        return -1
    elif Fecha2 < (Fecha1):
        return 1
    else:
        return 0

