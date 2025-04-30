import pandas as pd  
import matplotlib.pyplot as plt  

df = pd.read_csv('data.csv') 

#Cria Figura e Eixos explicitamente
fig, ax = plt.subplots()

#Associa o plot aos eixos criados
df['idade'].plot(kind='hist', ax=ax)
ax.set_title('Distribuição de Idades')  

#Salva Figura
fig.savefig('grafico.png')

#Fecha a figura para liberar memória
plt.close()

