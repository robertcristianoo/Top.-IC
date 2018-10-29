# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:50:37 2018

@author: Asus
"""

import pandas
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

enade2017=pandas.read_csv("datasets\MICRODADOS_ENADE_2017.txt", sep=';',dtype={"DS_VT_ESC_OFG": str, 
                                                                               'DS_VT_ESC_OCE':str,
                                                                              'DS_VT_ACE_OCE':str,
                                                                              'NT_GER':str,
                                                                              'NT_FG':str,
                                                                              'NT_OBJ_FG':str,
                                                                              'NT_DIS_FG':str,
                                                                              'NT_CE':str,
                                                                              'NT_OBJ_CE':str,
                                                                              'NT_DIS_CE':str})


enade2017.shape
enade2017.columns[0:10]

tabela = pandas.DataFrame(enade2017, columns=['NT_GER', 'CO_CATEGAD', 'CO_GRUPO'])
#print(tabela.head(10))

##limpeza dos dados
#substitui vírgula por ponto
tabela['NT_GER'] = tabela['NT_GER'].str.replace(',', '.')
#print (tabela['NT_GER'])

#observe os NaN (not a number)

'''No arquivo 'Dicionário de variáveis dos Microdados do Enade_Edição 2017' descreve que:
o codigo 222 no campo TP_PR_GER significa ausente 
556 e 888 são participações desconsideradas.
Portanto, algumas notas podem ser desconsideradas dependendo do seu objetivo, 
e aqui, será de calcular a média daqueles que fizeram a prova.
'''
tabela=tabela.loc[(tabela['NT_GER'].notnull())]
#print(tabela['NT_GER'])
#converte de str para float
tabela['NT_GER'] = pandas.to_numeric(tabela['NT_GER'])
#print(tabela['NT_GER'])
#print(tabela['NT_GER'].mean())

#print(tabela['NT_GER'].describe())

#outros comandos
#aux = tabela['NT_GER'].idxmax()
#print('indice da primeira maior nota: ', aux)
#print('Maior nota: ', tabela['NT_GER'][aux])


#Calcula a média de um curso especifico
#Código da área de enquadramento do curso no Enade == ciencia da computacao

ccomp = tabela[tabela['CO_GRUPO']==4004]

#print('\n',ccomp)
#print('\n',ccomp['NT_GER'].describe())

#ALUNOS COMPUTAÇÃO FEDERAL
cc_federal = tabela[tabela['CO_CATEGAD'] == 1]
cc_federal = cc_federal.loc[tabela['CO_GRUPO'] == 4004]
print(cc_federal.NT_GER.describe())

#Plot
plt.hist(cc_federal.NT_GER, 100, normed=True, color='green')
plt.title('Instituições Federais')
plt.show()

#ALUNOS COMPUTAÇÃO NÃO FEDERAL
cc_part = tabela[tabela['CO_CATEGAD'] != 1]
cc_part = cc_part.loc[tabela['CO_GRUPO'] == 4004]
print(cc_part.NT_GER.describe())

#Plot
plt.hist(cc_part.NT_GER, 100, normed=True, color='skyblue')
plt.title('Instituições NÃ0 Federais')
plt.show()

#ALUNOS COMPUTAÇÃO ESTADUAL
cc_partE = tabela[tabela['CO_CATEGAD'] == 2]
cc_partE = cc_partE.loc[tabela['CO_GRUPO'] == 4004]
print(cc_partE.NT_GER.describe())

plt.hist(cc_partE.NT_GER, 100, normed=True, color='magenta')
plt.title('Instituições Estaduais')
plt.show()

#ALUNOS COMPUTAÇÃO PRIVADA LUCRATIVA
cc_partPL = tabela[tabela['CO_CATEGAD'] == 4]
cc_partPL = cc_partPL.loc[tabela['CO_GRUPO'] == 4004]
print(cc_partPL.NT_GER.describe())

plt.hist(cc_partPL.NT_GER, 100, normed=True, color='orange')
plt.title('Instituições Privadas Lucrativas')
plt.show()

#ALUNOS COMPUTAÇÃO PRIVADA N LUCRATIVO
cc_partPNL = tabela[tabela['CO_CATEGAD'] == 5]
cc_partPNL = cc_partPNL.loc[tabela['CO_GRUPO'] == 4004]
print(cc_partPNL.NT_GER.describe())

plt.hist(cc_partPNL.NT_GER, 100, normed=True, color='blue')
plt.title('Instituições Privadas Não Lucrativas')
plt.show()

#Median and Max
print('\nMEDIANA Federal',cc_federal.NT_GER.median())
print('\nMEDIA Federal',cc_federal.NT_GER.mean())
print('\nMAX Federal',cc_federal.NT_GER.max())

print('\nMEDIANA Não Federal',cc_part.NT_GER.median())
print('\nMEDIA Não Federal',cc_part.NT_GER.mean())
print('\nMAX Não Federal',cc_part.NT_GER.max())

print('\nMEDIANA Estadual',cc_partE.NT_GER.median())
print('\nMEDIA Estadual',cc_partE.NT_GER.mean())
print('\nMAX Estadual',cc_partE.NT_GER.max())

print('\nMEDIANA Privada Lucrativa',cc_partPL.NT_GER.median())
print('\nMEDIA Privada Lucrativa',cc_partPL.NT_GER.mean())
print('\nMAX Privada Lucrativa',cc_partPL.NT_GER.max())

print('\nMEDIANA Privada NÃO Lucrativa',cc_partPNL.NT_GER.median())
print('\nMEDIA Privada NÃO Lucrativa',cc_partPNL.NT_GER.mean())
print('\nMAX Privada NÃO Lucrativa',cc_partPNL.NT_GER.max())

#plot Median and max

data = [[cc_federal.NT_GER.max(), cc_federal.NT_GER.median(), cc_federal.NT_GER.mean()],
  [cc_part.NT_GER.max(), cc_part.NT_GER.median(), cc_part.NT_GER.mean()]]

X = np.arange(3)
plt.bar(X + 0.00, data[0], color = 'g', width = 0.25, label='Federal')
plt.bar(X + 0.25, data[1], color = 'orange', width = 0.25, label='Não Federal')
plt.title('Instituições Federais vs. Não Federais')
plt.xticks([0,1,2],['Máxima','Mediana', 'Média'])
plt.legend()
plt.grid()
plt.show()

#PLOTS - visualization

import pylab as P
x = (cc_federal.NT_GER, cc_partE.NT_GER, cc_partPL.NT_GER, cc_partPNL.NT_GER)

n, bins, patches = P.hist(x, 10, normed=1, histtype='bar',
                            color=['green', 'magenta', 'orange', 'blue'],
                            label=['Federal', 'Estadual', 'Part.Luc.', 'Part.NLuc.'])
P.legend()
P.title('Comparativo de Resultados')
#plt.hist()

teste = pandas.DataFrame(ccomp, columns=['NT_GER', 'CO_CATEGAD'])

teste.NT_GER.hist()

# teste não paramétrico são métodos que não assumem uma distribuição específica para os dados.
stat, p = stats.mannwhitneyu(teste.NT_GER.loc[teste['CO_CATEGAD'] == 1], teste.NT_GER.loc[teste['CO_CATEGAD'] != 1])

print('Mann-Whitney: Estatisticas=%.3f, p=%.3f' % (stat, p))

alpha = 0.05
if p > alpha:
	print('Mesma distribuição')
else:
	print('Distribução diferente')
    
stat, p = stats.kruskal(teste.NT_GER.loc[teste.CO_CATEGAD == 1], teste.NT_GER.loc[teste.CO_CATEGAD != 1])
print('Kruskal-Wallis: Estatisticas=%.3f, p=%.3f' % (stat, p))

if p > alpha:
	print('Mesma distribuição')
else:
	print('Distribução diferente')
    
#anova
stat, p = stats.f_oneway(teste.NT_GER.loc[teste.CO_CATEGAD == 1], teste.NT_GER.loc[teste.CO_CATEGAD != 1])
print('Anova: Estatisticas=%.3f, p=%.3f' % (stat, p))
if p > alpha:
	print('Mesma distribuição')
else:
	print('Distribução diferente')
