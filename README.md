# zonaProp-AnalisisDeDatos
Un scraper que recopila los datos de todas las casas de una ciudad de una provincia de Argentina, para luego usar analisis de datos.

Como estamos en zonaprop trabajamos con argentina, las zonas seran ciudades de las provincias de argentina.

Importar las siguientes librerias:
'
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import os
import unicodedata
'
Luego de que corra el codigo se creara una tabla de excel preparada para convertir a csv (todos los elementos en la primera columna extendiendose por las filas).

El formato en el que deben ingresar la ciudad a buscar es en formato (sin mayusculas):
ejemplos:

san isidro
virreyes
