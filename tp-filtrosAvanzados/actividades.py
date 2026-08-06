import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Vote_Ai.csv")

#Actividad 1
filas = df.shape
columnas = df.shape

print(f"La tabla contiene {filas} filas y {columnas} columnas.\n")



#Actividad 2
filtro_avanzado = df["Attack_Type"] == "Cyber Attack"
df_filtro = df[filtro_avanzado]

print(df_filtro.head())

print(df["Attack_Type"].unique())