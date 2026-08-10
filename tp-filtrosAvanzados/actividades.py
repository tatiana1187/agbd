import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Vote_Ai.csv")

#Actividad 1

filas = df.shape
columnas = df.shape
print("\n Actividad 1")
print(f"La tabla contiene {filas} filas y {columnas} columnas.\n")


#Actividad 2
print("\n Actividad 2")
filtro_avanzado = df["Attack_Type"] == "Cyber Attack"
df_filtro = df[filtro_avanzado]

print(df_filtro.head())

#Actividad 3
print("\n Actividad 3")
filtro_avanzado = df["Attack_Type"].str.startswith("Cyber", na=False)
df_filtro = df[filtro_avanzado]
print(df_filtro.head())

#Actividad 4
print("\n Actividad 4")
resultado = df_filtro[["Attack_Type", "Total_Votes"]]
print(resultado.head())

#Actividad 5
print("\n Actividad 5")
grupo = df.groupby("Attack_Type")["Total_Votes"].sum()
grupo = grupo.sort_values(ascending=False)
print(grupo)

#Actividad 6
print("\n Actividad 6")
suma_total = df_filtro["Total_Votes"].sum()
limite = 50000000

if (total_critico := suma_total) > limite:
    print("Prioridad Alta")
else:
     print("Estado Normal")

print(f"Total de votos filtrados: {suma_total}")

#Actividad 7
print("\n Actividad 7")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df,
    x="Attack_Type",
    y="Total_Votes",
    estimator=sum,
    palette="viridis")


plt.title("Total de Votos por Tipo de Ataque", fontsize=14)
plt.xlabel("Tipo de Ataque", fontsize=12)
plt.ylabel("Total de Votos", fontsize=12)
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig("reporte_barras.png", dpi=300)
plt.close()



