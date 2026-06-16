import pandas as pd #importo pandas
import matplotlib.pyplot as plt
import seaborn as sns



#imprimo el archivo
#print("OKEY! Archivo cargado correctamente")
#mostrar las primeras filas del dataframe
#print (df.head())# imprimo toda la tabla

#filtra por año 2022
#resultado = df [df['Age']<50]
#print (resultado)
#imprime las columnas
#print(df.columns)
#total_hadware = df['Postal_Vote_Ratio'].count()
#print(f"Total de registros {total_hadware}")

#total_votos = df['Total_Votes'].sum()
#print(f"Total de votos: {total_votos}")

# print("---Analisis Avanzado de Datos---")










df=pd.read_csv("Vote_Ai.csv")

#-----LOGICA DE FILTRADO------ 
filtro_avanzado = df['Attack_Type'].str.startswith('Cyber',na=False)
df_filtro= df[filtro_avanzado]
sumo_dinero=df_filtro['Campaign_Spending_Cr'].sum()
print("--reporte financiero automatico--")
print(f"monto total analizado:{sumo_dinero: .2f} millones. \n")
 
 #filtro_numero=df['Campaign_Spending_Cr'] > 500


#-----CONDICIONAL------
if default_limite_Alto := (sumo_dinero > 500):
    print("¡Alerta! el monto total supera el limite establecido")
    print("Requiere revision inmediata")
elif sumo_dinero < 100:
    print("Aviso:mercado moderado/alto")
    print("Monitoriar comportamiento prox tria")
else:
    print("Mercado estable, sin alertas por el momento")

#-------GRAFICO DE BARRAS USANDO TODA DF---------
print("\n[Generando GRAFICO de barras ]")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(
 data=df,
 x="Party",
 y="Campaign_Spending_Cr",
 estimator=sum,
 errorbar=None,
 palette= "viridis"
)
plt.title("Gasto Total de Campaña por Partido Político", fontsize=14)
plt.xlabel("Partido Político", fontsize=12)
plt.ylabel("Gasto Total (en millones)", fontsize=12)
plt.xticks(rotation=20)

#----------GUARDO GRAFICO GENERADO--------
plt.savefig("garafico_barra.png",dpi=300)
plt.close()
print("\n¡Hecho! Los graficos se guardaron correctamente en tu carpeta")