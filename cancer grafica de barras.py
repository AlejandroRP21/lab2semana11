import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv("cancer-probabilities.csv")
fr = df["Smoking Habit"].value_counts()
plt.ylabel("habitos de fumar")
plt.title("probabilidad de desarrollar cancer")
plt.bar(fr.index,fr.values)
plt.show()

#link del dataset https://www.kaggle.com/datasets/tusharkute/cancer-probabilities
#columna seleccionada: habitos de fumar 
#grafico de barras
#analisis: en la grafica se puede ver que tan probable es que tengas cancer por tu habito de fumar 
#en la grafica heavy se puede observar que es alta la probabilidad de obetener cancer ya que se podria decir que fumar 
#de forma de frecuente podria generar alta probabilidad de cancer 
# en la segunda se ve que fumar de manera moderadamente de igual forma hay una alta probabiliddd de desarrollar cancer 
# en la ultima grafica se ve que fumar de manera ocacional hay baja probabilidad de desarrollar cancer pero siempre hay 
#la probabilidad de que suceda

