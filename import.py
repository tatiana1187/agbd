import pandas as pd #importo pandas

df=pd.read_csv("Vote_Ai.csv")
#imprimo el archivo
print("OKEY! Archivo cargado correctamente")
#mostrar las primeras filas del dataframe
print (df.head())# imprimo toda la tabla

#filtra por año 2022
resultado = df [df['Age']<50]
print (resultado)
#imprime las columnas
#print(df.columns)
#total_hadware = df['Postal_Vote_Ratio'].count()
#print(f"Total de registros {total_hadware}")



total_votos = df['Total_Votes'].sum()

print(f"Total de votos: {total_votos}")
