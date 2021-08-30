import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests


#Importar el dataframe de los ascensos al everest
ascensos_everest = pd.read_csv("Mt_Everest_Ascent_Data.csv")

#Quitar los espacios del principio/final y reemplazar los del centro por barrabajas.
def column_cleaning(df):
    df.columns = [col.strip().replace(" ", "_") for col in df.columns]
    return df

#Función que devuelve el primer elemento de una columna (Yr/Seas)
def separación_year(year_season):
    return year_season.split()[0]

#Función que devuelve el segundo elemento de una columna (Yr/Seas)
def separación_season(year_season):
    return year_season.split()[1]   

#Función que devuelve el segundo elemento de una columna separada por (-) "Date"
def separación_Date(day_month):
        return day_month.split("-")[1]

#Función que devuelve el primer elemento de una columna separada por (-) "Date"
def separación_Date1(day_month):
        return day_month.split("-")[0]

#Función que reemplaza ciertos valores con el fin de tener mayor claridad. 
def replacements(df):
    df = df.replace('Y','Yes')
    df.Age = df.Age.replace(0, "NaN")
    df.Dth = df['Dth'].replace('.','No')
    return df

#Función que crea el dataframe final solo con las columnas que quiero.
def escoger_columnas(df):
    df = df[['Peak', 'Name', 'Citizenship', 'Sex', 'Age',
       'Oxy', 'Dth', 'Host', 'Year', 'Season', 'Month', 'Day','Time']]
    return df

#Función que devuelve crea columnas nuevas basadas en columnas antiguas spliteadas. 
def cleaning_dataframe(df):
    df = column_cleaning(df)
    df = replacements(df)
    df["Season"] = df["Yr/Seas"].apply(separación_season)
    df["Year"] = df["Yr/Seas"].apply(separación_year)
    df["Month"] = df.Date.apply(separación_Date)
    df["Day"] = df.Date.apply(separación_Date1)
    df = escoger_columnas(df)
    return df

