# **************************************************
# Trabalho 01 Introdução IC
# Equipe: Anne Almeida, Giovane Richard e Robert Cristiano
# Professora: Luciana Balieiro
# Algoritmo: REGRESSÃO LINEAR
# **************************************************

from sklearn import linear_model
from sklearn.datasets import load_wine
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wine = load_wine()
#itens da base
wine.keys()

#print(wine.DESCR)

tabela = pd.DataFrame(wine.data)
tabela.columns = wine.feature_names
tabela["Target"] = wine.target
#print(tabela)

#dados = wine['data']
#classif = wine['target']

#descri = {'Álcool', 'Ácido Málico', 'Ash', 'Alcali', 'Magnésio', 'Fenóis', 'Flavonóides', 'NonFenóis', 'Proantocianinas', 'Intensi-cor', 'HUE', 'OD280/OD315 ', 'Prolina'}

#tabela = pd.DataFrame(dados, columns=descri)

#Descrição do Index
tabela.index 
#Colunas presentes no DataFrame
#tabela.columns 
tabela.head(35)

# MOSTRANDO AS CORELAÇÕES GRAFICAMENTE

# plt.scatter(tabela['Álcool'], tabela['Intensi-cor'])
# plt.xlabel('Álcool')
# plt.ylabel('ácido málico')
# plt.show()

sns.lmplot("alcalinity_of_ash", "flavanoids", tabela, scatter_kws={"marker":"x", "color":"blue"},
          line_kws={"linewidth":1, "color": "orange"})

sns.lmplot("od280/od315_of_diluted_wines", "color_intensity", tabela, scatter_kws={"marker":"x", "color":"blue"},
          line_kws={"linewidth":1, "color": "orange"})

sns.lmplot("alcohol", "color_intensity", tabela, scatter_kws={"marker":"x", "color":"blue"},
          line_kws={"linewidth":1, "color": "orange"})

#Métodos de correlação
tabela.corr()
# Visualiza a tabela de correlação gerada
#print(tabela.corr())
# Correlacionando por cores
#sns.heatmap(tabela.corr())

# Selecionando 2 colunas 
X = tabela[["alcalinity_of_ash", "flavanoids"]]
#print(X)

# LEMBRETE --> precisamos escolher a variável para fazer a correlação

#separa em dois conjuntos, um para treinamento e outro para validação (20 últimos)
X_t = X[:-20]
X_v = X[-20:]

y_t = tabela["Target"][:-20]
y_v = tabela["Target"][-20:]

# função de regressão linear
regr = linear_model.LinearRegression()

# treina o modelo
regr.fit(X_t, y_t)

# faz a predição
y_pred = regr.predict(X_v)

# coeficientes a
print('Coeficientes: \n', regr.coef_)
#intercepto b
print('Coeficientes: \n', regr.intercept_)
#y = -0.03423418*alcohol - 0.00140247*proline + 2.31
#prediz manualmente os valores com base nos coeficientes encontrados na regressao
y_teste = 0.0574*X_v["alcalinity_of_ash"] - 0.5533*X_v["flavanoids"] + 0.9125
#exibe o valor predito manualmente y_teste, que começa de 486
#exibe o valor real y_t
#exibe o valor predito pela regressão linear

print(y_teste[158], y_t[0],y_pred[0])

#plota todos os valores de validação
#plt.scatter(X_v["flavanoids"], y_v,  color='black')
#plt.scatter(X_v["flavanoids"], y_pred, color='blue')
#plt.legend(["Real", "Predito"])