# main.py

import numpy as np
import random
import print_resultados
import Iniciar_dados as init
import Gerar_solucao as solution
import functions as func
import copy
import solucaoInicial

#OBJETIVO_OTIMIZACAO = "numero_pas" 
OBJETIVO_OTIMIZACAO = "distancias" 

VIZINHANCA = [1,2,3,4]
    
def vnd(x, k_max):
    fitness_evolution = []
    k = 1
    print(solution.avaliar_fit(solution.get_solution(x)[0]))

    while(k <= k_max):
        print("K = ", k)
        vetor_solucoes = []
        vetor_prioridades = []

        for i in range(50):
            vetor_prioridades.append(copy.deepcopy(func.shake(list(x), VIZINHANCA[2], OBJETIVO_OTIMIZACAO)))
            vetor_solucoes.append(solution.avaliar_fit(solution.get_solution(vetor_prioridades[i])[0]))

        indice = min(enumerate(vetor_solucoes), key=lambda x: x[1][0])[0]
        x_linha = vetor_prioridades[indice]
        
        x, k = func.neighborhood_change(x, x_linha, k, OBJETIVO_OTIMIZACAO)
        fitness_evolution.append(solution.avaliar_fit(solution.get_solution(x)[0]))
        print(solution.avaliar_fit(solution.get_solution(x)[0]))

    return x, fitness_evolution



solucao_inicial = solucaoInicial.gerar_sol_inicial(OBJETIVO_OTIMIZACAO)
solutions = []
for i in range(10):
    solutions.append(vnd(solucao_inicial, len(VIZINHANCA)))

# plotar resultados
for solucao in solutions:
    fitness = solution.get_solution(solucao[0])
    print_resultados.print_solucao(fitness[0])
    print_resultados.print_plano_cartesiano(fitness[0])
    print_resultados.plot_pas(fitness[0])
    print_resultados.plotar_resultados_otimizacao(solucao[1])