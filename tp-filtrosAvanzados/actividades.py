import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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


#Actividad 8
print("\n Actividad 8")
datos_torta = grupo.nlargest(5)
plt.figure(figsize=(8, 8))

plt.pie(
    datos_torta.values,
    labels=datos_torta.index,
    autopct="%1.1f%%",
    wedgeprops={"edgecolor": "white"}
)
plt.savefig("reporte_torta.png", dpi=300)
plt.close()
print("Gráfico de torta guardado como reporte_torta.png")

#Actividad 9
print("\n Actividad 9")
condicion_extra = df['Campaign_Spending_Cr'] > 5
resultado = df.loc[
    filtro_avanzado & condicion_extra,
    ['State', 'Party', 'Campaign_Spending_Cr']
]
print(resultado.head())
print(f"\nFilas seleccionadas: {len(resultado)}")

#Actividad 10
print("\n Actividad 10")
print(df.isnull().sum())

df_con_nulos = df.copy()
print("\nNulos en Campaign_Spending_Cr después de la comprobación:")
print(df_con_nulos['Campaign_Spending_Cr'].isnull().sum())

df_sin_nulos = df_con_nulos.dropna()
media = df_con_nulos['Campaign_Spending_Cr'].mean()
df_rellenado = df_con_nulos.fillna(
    {'Campaign_Spending_Cr': round(media, 2)}
)
print(f"\nOriginal: {len(df_con_nulos)} filas")
print(f"Con dropna: {len(df_sin_nulos)} filas (se eliminaron filas)")
print(f"Con fillna: {len(df_rellenado)} filas (se rellenaron los huecos)")

#Actividad 11
print("\n Actividad 11")
agrupado_lineas = df.groupby('Party')['Campaign_Spending_Cr'].sum().sort_values()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    agrupado_lineas.index,
    agrupado_lineas.values,
    marker='o',
    linewidth=2,
    markersize=8
)

idx_max = agrupado_lineas.idxmax()
val_max = agrupado_lineas.max()
x_pos = list(agrupado_lineas.index).index(idx_max)

ax.annotate(
    f'Máximo: {val_max:,.0f}',
    xy=(idx_max, val_max),
    xytext=(x_pos - 2.5, val_max * 0.85),
    arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
    fontsize=11,
    color='red',
    fontweight='bold'
)

ax.set_title('Gasto total por partido', fontsize=14, fontweight='bold')
ax.set_xlabel('Partido')
ax.set_ylabel('Total de gasto')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('grafico_lineas.png', dpi=150)
plt.close()

#Actividad 12
print("\n Actividad 12")

resultado_original = df[(df['Campaign_Spending_Cr'] > 5) & (df['Party'] == 'BJP')]

valor_limite = 5
partido_var = 'BJP'
resultado_query = df.query('Campaign_Spending_Cr > @valor_limite and Party == @partido_var')

print("Con corchetes (filas):", len(resultado_original))
print("Con .query() (filas):", len(resultado_query))
print("¿Son exactamente iguales?:", resultado_original.equals(resultado_query))

#Actividad 13
print("\nActividad 13")

categorias_elegidas = ['BJP', 'INC', 'AAP']
df_incluidos = df[df['Party'].isin(categorias_elegidas)]

df_excluidos = df[~df['Party'].isin(categorias_elegidas)]

print(f"Filas incluidas ({len(df_incluidos)}):")
print(f"Filas excluidas ({len(df_excluidos)}):")

total = len(df)
suma = len(df_incluidos) + len(df_excluidos)
print(f"Total original: {total} | Incluidos + Excluidos: {suma}")
print(f"¿Coinciden el total y la suma?: {total == suma}")

#Actividad 14
print("Value Counts:\n", df['Party'].value_counts())
print("\nValores únicos:\n", df['Party'].unique())
print("\nCantidad de categorías distintas:", df['Party'].nunique())
print("\nPorcentajes (%):\n", (df['Party'].value_counts(normalize=True) * 100).round(1))

df_filtrado = df[filtro_avanzado]
print("Value Counts:\n", df_filtrado['Party'].value_counts())
print("\nValores únicos:\n", df_filtrado['Party'].unique())
print("\nCantidad de categorías distintas:", df_filtrado['Party'].nunique())
print("\nPorcentajes (%):\n", (df_filtrado['Party'].value_counts(normalize=True) * 100).round(1))

#Actividad 15
print("\n Actividad 15")

df_filtrado = df[filtro_avanzado]
df_filtrado.to_csv("resultado_filtrado.csv", index=False)
print(f"\nArchivo exportado: {len(df_filtrado)} filas guardadas.")

correlacion = df.corr(numeric_only=True)

print("\nMatriz de correlación:")
print(correlacion.round(2))

plt.figure(figsize=(16, 12))

sns.heatmap(
    correlacion,
    annot=True,
    fmt=".2f",
    cmap="viridis",
    linewidths=0.5,
    vmin=-1,
    vmax=1
)

plt.title(
    "Correlación entre variables - Vote AI",
    fontweight="bold"
)

plt.tight_layout()
plt.savefig("heatmap_vote_ai.png", dpi=300)
plt.close()

print("\nHeatmap guardado como heatmap_vote_ai.png")

mask = np.triu(
    np.ones(correlacion.shape),
    k=0
).astype(bool)

correlacion_sin_diag = correlacion.where(~mask)

par_max = correlacion_sin_diag.stack().idxmax()
par_min = correlacion_sin_diag.stack().idxmin()

print(f"\nPar más correlacionado: {par_max[0]} ↔ {par_max[1]}")
print(f"Par menos correlacionado: {par_min[0]} ↔ {par_min[1]}")




