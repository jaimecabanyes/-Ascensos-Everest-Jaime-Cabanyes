# W3
W3 README

Everest
Este trabajo analiza una serie de datos sobre todos los alpinistas que han alcanzado la cima del Everest. El Everest es el punto terrestre mas alto del mundo, contando con una altitud de 8,848 metros.

Dataframe
El dataframe contiene variables como (Pico, Nombre, Origen, Género, Edad, Oxígeno, Mortalidad, País de entrada, Año, Estación, Mes, Día y Hora.)
Para limpiar el dataframe original, han sido requeridas ciertas funciones que han hecho del dataframe original un dataframe mas limpio y cómodo, facilitando su uso. 

Diferentes Partes del Trabajo
1.	Un archivo.py llamado funciones_limpieza.py dentro de la carpeta src que contiene todas las funciones que han sido utilizadas para limpiar el dataframe original.
2.	Un archivo llamado main.py que llama a todas las funciones anteriormente dichas que limpia el dataframe en una sola función.
3.	Un archivo.ipynb llamado DataFrame cleaning.ipynb que  contiene las mismas funciones que el archivo funciones_limpieza.py, sin embargo ese archivo exporta el resultado de todas las funciones aplicadas  a un csv nuevo dentro de la carpeta Data llamado ascensos_everest_final.csv.
4.	El trabajo también contiene un archivo.ipynb llamado WEB Scraping.ipynb Aquí, una serie de procedimientos se hacen para sacar información extra de los casos de mortalidad en el Everest. De la página web, se sacan 3 tablas distintas que son exportadas a la carpeta de Data. (table1, table2, table3).
5.	Finalmente, tenemos la visualización.ipynb. Esto es un archivo que llama a todas las variables y data.csv previamente creados para mostrar los datos de una manera visual. 

Librerías Utilizadas 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import regex as re
import requests
from bs4 import BeautifulSoup
