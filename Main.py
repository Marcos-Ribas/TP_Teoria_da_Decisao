# main.py

import numpy as np
import random
import print_resultados
import Iniciar_dados as init
import Gerar_solucao as solution
import functions as func
import copy

#OBJETIVO_OTIMIZACAO = "numero_pas" 
OBJETIVO_OTIMIZACAO = "distancias" 

VIZINHANCA = [1,2,3]
    
def vnd(x, k_max):
    fitness_evolution = []
    k = 1
    print(solution.avaliar_fit(solution.get_solution(x)[0]))

    while(k <= k_max):
        print("K = ", k)
        vetor_solucoes = []
        vetor_prioridades = []

        for i in range(10):
            vetor_prioridades.append(copy.deepcopy(func.shake(list(x), VIZINHANCA[2])))
            vetor_solucoes.append(solution.avaliar_fit(solution.get_solution(vetor_prioridades[i])[0]))

        indice = min(enumerate(vetor_solucoes), key=lambda x: x[1][0])[0]
        x_linha = vetor_prioridades[indice]
        
        x, k = func.neighborhood_change(x, x_linha, k, OBJETIVO_OTIMIZACAO)
        fitness_evolution.append(solution.avaliar_fit(solution.get_solution(x)[0]))
        print(solution.avaliar_fit(solution.get_solution(x)[0]))

    return x, fitness_evolution



vetor_prioridades = np.random.permutation(6400)

solucao = vnd(vetor_prioridades, 3)

# plotar resultados

fitness = solution.get_solution(solucao[0])

print_resultados.print_solucao(fitness[0])
print_resultados.print_plano_cartesiano(fitness[0])
print_resultados.plot_pas(fitness[0])
print_resultados.plotar_resultados_otimizacao(solucao[1])