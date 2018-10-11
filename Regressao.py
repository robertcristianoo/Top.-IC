# **************************************************
# Trabalho 01 Introdução IC
# Equipe: Anne Almeida, Giovane Richard e Robert
# Professora: Luciana Balieiro
# Algoritmo: REGRESSÃO LINEAR
# **************************************************

from sklearn import linear_model
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
from pprint import pprint


wine = load_wine()
#itens da base
wine.keys()

#print(wine.DESCR)

#tabela = pandas.DataFrame(wine.data)
#tabela.columns = wine.target_names

dados = wine['data']
classif = wine['target']

descri = {'Álcool', 'ácido málico', 'Ash', 'Alcali', 'Magnésio', 'fenóis ', 'flavonóides', 'Fen não flav', 'Proantocianinas', 'intensi-cor', 'matiz', 'OD280/OD315 ', 'prolina'}

tabela = pd.DataFrame(dados, columns=descri)

#Descrição do Index
tabela.index 
#Colunas presentes no DataFrame
#tabela.columns 

# adicionando a coluna de Preço
#tabela['Preço'] = y
tabela.head(10)



# Mostrando graficamente
plt.scatter(tabela['Álcool'], tabela['intensi-cor'])
plt.xlabel('Álcool')
plt.ylabel('ácido málico')
plt.show()

#Métodos de correlação
tabela.corr()

# Selecionando 2 colunas 
X = tabela[["Álcool", "intensi-cor"]]
print(k)

# LEMBRETE --> precisamos escolher a variável para fazer a correlação

#separa em dois conjuntos, um para treinamento e outro para validação (20 últimos)
X_t = k[:-20]
X_v = k[-20:]

#print(X_t["RM"])
y_t = tabela["intensi-cor"][:-20]
y_v = tabela["intensi-cor"][-20:]

# função de regressão linear
regr = linear_model.LinearRegression()

# treina o modelo
regr.fit(X_t, y_t)

# faz a predição
y_pred = regr.predict(X_v)

# Mostrar o resultado final em um Histograma
# plt.hist(tabela['Álcool'], color='blue', bins=20)
# plt.title('Histograma da variável resposta')
# plt.show()