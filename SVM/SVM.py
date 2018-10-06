# **************************************************
# Trabalho 01 Introdução IC
# Equipe: Anne Almeida, Giovane Richard e Robert
# Professora: Luciana Balieiro
# Algoritmo: SUPORTE VECTOR MACHINE - SVM
# **************************************************

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix
import numpy


iris = datasets.load_iris()
# Lendo exatamente 3 característica da base
caract = iris.data[:, :3]
classifi = iris.target

plt.subplots()
plt.scatter(caract[:, 0], caract[:, 1], c=classifi, cmap=plt.cm.Set1)
plt.xlabel('Comprimento Sepala')
plt.ylabel('Largura Sepala')
plt.grid(True)
plt.show()

# Classificador
clf = svm.SVC(gamma=0.001, C=100)

# Dados para treinamento 40 de cada classe
carac_treino = numpy.concatenate([caract[:40,:], caract[51:90,:], caract[101:140,:]])
classif_treino = numpy.concatenate([classifi[:40], classifi[51:90], classifi[101:140]])

clf.fit(carac_treino, classif_treino)

# Classificação dos dados de teste
x_testes = numpy.concatenate([caract[40:50,:], caract[90:100,:], caract[140:150,:]])
y_testes =numpy.concatenate([classifi[40:50], classifi[90:100], classifi[140:150]])

yp = clf.predict(x_testes)

print(yp)
print(y_testes)

# impressão da Matriz de confusão e dos dados da classificação
print('\n\nMatriz de Confusão:\n\n', confusion_matrix(y_testes, yp))
print('\n\n', classification_report(y_testes, yp))
