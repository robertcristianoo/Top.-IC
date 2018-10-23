# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 07:43:30 2018

@author: IFNMG
"""

import pandas
import matplotlib.pyplot as plt

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

tabela = pandas.DataFrame(enade2017, columns=['NT_GER', 'CO_CATEGAD', 'CO_GRUPO', 'QE_I08', 'CO_IES', 'QE_I05'])
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
aux = tabela['NT_GER'].idxmax()
#print('indice da primeira maior nota: ', aux)
#print('Maior nota: ', tabela['NT_GER'][aux])


#Calcula a média de um curso especifico
#Código da área de enquadramento do curso no Enade == ciencia da computacao

ccomp = tabela[tabela['CO_GRUPO']==4004]

#print(ccomp)

#print(ccomp['NT_GER'].describe())

#do curso do IFNMG
ifccomp = ccomp[ccomp['CO_IES']==3188]
#print(ifccomp.describe())

#somente as notas de quem respondeu a questão sobre a renda
ccomp=ccomp.loc[(ccomp['QE_I08'].notnull())]
#print(ccomp.NT_GER.describe())

ccomp.QE_I08.head(10)

ccomp['QE_I08'] = ccomp['QE_I08'].map({'A': 1, 'B': 2, 'C': 3, 'D': 4,'E': 5, 'F':6,'G':7})

#print(ccomp.QE_I08.head(10))

#visualmente
#plt.scatter( ccomp.NT_GER, ccomp.QE_I08)
#plt.ylabel('Faixa de renda')
#plt.xlabel('Nota do curso de C. da Comp.')
#plt.show()

#ESCOLARIDADE DA MÃE
ccomp.QE_I05 = ccomp['QE_I05'].map({'A': 1, 'B': 2, 'C': 3, 'D': 4,'E': 5, 'F':6})

#print(ccomp.QE_I05.head(10))

#visualmente
#plt.scatter(ccomp.QE_I05, ccomp.NT_GER)
#plt.ylabel('Nota do curso de C. da Comp.Escolaridade da mãe')
#plt.xlabel('Escolaridade da mãe.')
#plt.show()

escolaridade = ccomp.loc[ccomp.QE_I05 == 1]
#print(escolaridade.NT_GER.describe())

#ALUNOS COMPUTAÇÃO FEDERAL
cc_federal = tabela[tabela['CO_CATEGAD'] == 1]
cc_federal = cc_federal.loc[tabela['CO_GRUPO'] == 4004]
print(cc_federal.NT_GER.describe())

#ALUNOS COMPUTAÇÃO NÃO FEDERAL
cc_part = tabela[tabela['CO_CATEGAD'] != 1]
cc_part = cc_part.loc[tabela['CO_GRUPO'] == 4004]
print(cc_part.NT_GER.describe())

#ALUNOS COMPUTAÇÃO ESTADUAL
cc_part = tabela[tabela['CO_CATEGAD'] == 2]
cc_part = cc_part.loc[tabela['CO_GRUPO'] == 4004]
print(cc_part.NT_GER.describe())

#ALUNOS COMPUTAÇÃO MUNICIPAL
cc_part = tabela[tabela['CO_CATEGAD'] == 3]
cc_part = cc_part.loc[tabela['CO_GRUPO'] == 4004]
print(cc_part.NT_GER.describe())

#ALUNOS COMPUTAÇÃO PRIVADA LUCRATIVA
cc_part = tabela[tabela['CO_CATEGAD'] == 4]
cc_part = cc_part.loc[tabela['CO_GRUPO'] == 4004]
print(cc_part.NT_GER.describe())

#ALUNOS COMPUTAÇÃO PRIVADA N LUCRATIVO
cc_part = tabela[tabela['CO_CATEGAD'] == 5]
cc_part = cc_part.loc[tabela['CO_GRUPO'] == 4004]
print(cc_part.NT_GER.describe())