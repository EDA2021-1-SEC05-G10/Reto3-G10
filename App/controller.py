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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newcatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    file = cf.data_dir + "UFOS/UFOS-utf8-small.csv"
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    lista=lt.newList()
    for info in input_file:
        model.add_cities(info, catalog)
        model.add_duration(info, catalog)
        model.add_duration_hours(info, catalog)
        model.add_years(info, catalog)
        model.add_location(info, catalog)
        model.add_long(info, catalog)
        lt.addLast(lista, info)
    return lista

        

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def requerimiento1(catalog, ciudad):

    return model.requerimiento1(catalog, ciudad)

def requerimiento2(catalog, tiempo_min, tiempo_max):

    return model.requerimiento2(catalog, tiempo_min, tiempo_max)

def requerimiento3(catalog, minimo, maximo):

    return model.requerimiento3(catalog, minimo, maximo)


def requerimiento4(catalog, tiempo_año_1, tiempo_año_2):

    return model.requerimiento4(catalog, tiempo_año_1, tiempo_año_2)

def requerimiento5(catalog,lonMin,lonMax,latMin,latMax):
    return model.requerimiento5(catalog,lonMin,lonMax,latMin,latMax)

def bono(catalog, longitud_max, longitud_min, latitud_min, latitud_max):

    return model.bono(catalog, longitud_max, longitud_min, latitud_min, latitud_max)