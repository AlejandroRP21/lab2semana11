import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("F1 2023.csv")

drivers = df["DRIVER"]  
ratings = df["RTG"]  

plt.plot(drivers, ratings, label='Calificación de los Conductores', marker='o')
plt.xlabel("Conductores")
plt.ylabel("Calificación (RTG)")
plt.title("Calificación de Conductores de F1 en 2023")



# Rotar las etiquetas del eje x para mejor visibilidad(Sacado de google)
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.tight_layout()  
plt.show()


#link del dataset: https://www.kaggle.com/datasets/riznofadhil2/drivers-rating-of-f1-21-to-f1-23
#grafica de lineas 
# en la grafica se ve la puntuacion de cada piloto por su desempeño durante toda la temporada 2023