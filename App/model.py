"""
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
import DISClib.DataStructures.linkedlistiterator as it
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newcatalog():
    catalog= {'cities': None, 'years':None, 'duration (seconds)': None, 'Horas': None }
    catalog['years']= om.newMap(omaptype='BST',comparefunction=compareDates)
    catalog['cities']= om.newMap(omaptype='BST',comparefunction=compareDates)
    catalog['duration (seconds)']= om.newMap(omaptype='BST',comparefunction=compareDates)
    catalog['horas']=om.newMap(omaptype='BST',comparefunction=compareDates)
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
                if elemento['datetime'] > lt.getElement(lista, i)['datetime']:
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
    while it.hasnext(iterator1):
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















# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareDates(Fecha1,Fecha2):
    if Fecha1 < (Fecha2):
        return -1
    elif Fecha2 < (Fecha1):
        return 1
    else:
        return 0

