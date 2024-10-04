import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("games_ranking.csv")
fr = df["rank_type"].value_counts()
plt.pie(fr.values, labels=fr.index, autopct="%1.1f%%")
plt.title("Distribución de juegos por tipo de ranking")
plt.show()
#link del dataset https://www.kaggle.com/datasets/mohamedtarek01234/steam-games-reviews-and-rankings
#grafica de barras
#columna seleccionada:  tipo de rango o rank type
#hay 3 tipos de datos ventas:  casi un tercio de los juegos se valoran por la cantidad de unidades vendidas, sin necesariamente considerar ingresos totales. 
# ganacias: un tercio de los juegos se evalúan principalmente en función de la cantidad de dinero que generan.
# y review: o que refleja que una parte importante del ranking se basa en la evaluación de la calidad o popularidad entre la audiencia.
#
