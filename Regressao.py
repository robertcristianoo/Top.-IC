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

print(wine.DESCR)

#tabela = pandas.DataFrame(wine.data)
#tabela.columns = wine.target_names

X = wine['data']
y = wine['target']

tabela = pd.DataFrame(X)


# adicionando a coluna de Preço
tabela['Preço'] = y
tabela.head(10)

# Mostrando graficamente
# plt.scatter(y, X)
# plt.xlabel('Quantidade de Alcool')
# plt.ylabel('Preço')
# plt.show()