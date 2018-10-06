# *************************************************
# Tópicos em IC
# Professora: Luciana Balieiro
# Equipe: Anne Almeida, Giovane Richard, Robert Cristiano
# Tema: Rastrigin - Algoritmo Genético 
# *************************************************

import random
import matplotlib.pyplot as plt
import numpy as np

#tamanho de cada indivíduo
dimensoes = 4
#quanto mais indíviduos, melhor a taxa de conversão pra 0
num_indivi = 50
#quanto mais gerações, melhor a taxa de conversão pra 0
num_geracoes = 1000
#chance de alterar um bit aleatório
taxa_mutacao = 0.5

#Gera individuos com valores entre [-5.12 a 5.12]
def geraPopulacao():
    populacao  = np.zeros((num_indivi, dimensoes))
    
    for i in range(num_indivi):
        for j in range(dimensoes):
            populacao[i,j] = np.random.uniform(-5.12, 5.12)
    
    return populacao

#Função objetiva rastrigin que minimiza
def fitness(X):
    fit = np.zeros((len(X), 1))
    
    for i in range(len(X)):
        ans = 0
        for j in range(0, 4):
            ans = ans + (X[i,j]*X[i,j]) - (10.0*np.cos(X[i,j]*2.0*np.pi))
            
        fit[i] = ans + (10*dimensoes)
    return fit
    
#Modo torneio
def selecao(X, fit):
    qtdPais = num_indivi
    
    pais = np.zeros((qtdPais, dimensoes))
    
    quantidade = 0
    
    while quantidade < qtdPais:
        filho1 = random.randrange(0,(num_indivi-1))
        filho2 = random.randrange(0,(num_indivi-1))
        
        if fit[filho1] < fit[filho2]:
            pais[quantidade,:] = X[filho1,:]
        else:
            pais[quantidade,:] = X[filho2,:]
            
        quantidade = quantidade + 1
    
    return pais

#Cruzamento por corte
def cruzamento(pais):
    num_pais = len(pais)
    filhos = np.zeros((num_pais, dimensoes))
    par = 0
    
    while par < num_pais:
        corte = random.randrange(2,(dimensoes - 1))
        filhos[par, 0:corte] = pais[par, 0:corte]
        filhos[par, corte:dimensoes] = pais[par+1, corte:dimensoes]
        filhos[par+1, 0:corte] = pais[par+1,0:corte]
        filhos[par+1, corte:dimensoes] = pais[par, corte:dimensoes]
        
        par = par + 2
        
    return filhos
    
#Se o numero gerado for menor que a taxa de mutação, altera o bit aleatório
def mutacao(X):
    for i in range(len(X)):
        if np.random.random() < taxa_mutacao:
            x = np.random.randint(0, 4)
            y = np.random.uniform(-5.12, 5.12)
            X[i, x] = y
            
    return X

def main():
    populacao = geraPopulacao()
    cont = 0
    
    melhores = np.zeros((num_geracoes, 1))
    
    # Avaliação de parada
    while cont < num_geracoes:
            fit = fitness(populacao)
            pais = selecao(populacao, fit)
            filhos = cruzamento(pais)
            filhos = mutacao(filhos)
            fitness_filhos = fitness(filhos)
        
            if min(fitness_filhos) < min(fit):
                melhor = filhos[np.argmin(fitness_filhos),:]
            else:
                melhor = populacao[np.argmin(fit),:]
        
            populacao[0,:] = melhor
            populacao[1:num_indivi,:] = filhos[1:num_indivi,:]
            melhores[cont] = np.min(fit)
        
            cont = cont + 1
        
    plt.plot(melhores)
    plt.show()
    
    print('\nMelhores: ', melhor)
    print('\nRastrigin(X): ', min(fit))

main()