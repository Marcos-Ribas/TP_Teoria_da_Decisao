import numpy as np
import random
import print_resultados
import Iniciar_dados as init
import Gerar_solucao as solution
import functions as func
import copy
import solucaoInicial
import time

OBJETIVO_OTIMIZACAO = "numero_pas" 
#OBJETIVO_OTIMIZACAO = "distancias" 

VIZINHANCA = [1,2,3,4]

def generate_numbers(total_numbers, low, high):
    # Lista para armazenar os números gerados
    result = []
    
    # Loop até obter o número total desejado
    while len(result) < total_numbers:
        # Gerar uma sequência de números únicos aleatórios entre low e high
        numbers = np.arange(low, high)
        np.random.shuffle(numbers)
        
        # Adicionar os números embaralhados à lista de resultados
        result.extend(numbers)
    
    # Cortar a lista para obter exatamente 'total_numbers' elementos
    return result[:total_numbers]

def vnd(x, k_max):
    fitness_evolution = []
    k = 1
    print(solution.avaliar_fit(solution.get_solution(x)[0]))

    while(k <= k_max):
        print("K = ", k)
        vetor_solucoes = []
        vetor_prioridades = []

        for i in range(30):
            vetor_prioridades.append(copy.deepcopy(func.shake(list(x), VIZINHANCA[2], OBJETIVO_OTIMIZACAO)))
            vetor_solucoes.append(solution.avaliar_fit(solution.get_solution(vetor_prioridades[i])[0]))

        indice = min(enumerate(vetor_solucoes), key=lambda x: x[1][0])[0]
        x_linha = vetor_prioridades[indice]
        
        x, k = func.neighborhood_change(x, x_linha, k, OBJETIVO_OTIMIZACAO)
        fitness_evolution.append(solution.avaliar_fit(solution.get_solution(x)[0]))
        print(solution.avaliar_fit(solution.get_solution(x)[0]))

    avaliacao = solution.avaliar_fit(solution.get_solution(x)[0])
    fronteira_pareto.append(avaliacao[:2])
    return x, fitness_evolution



solucao_inicial = solucaoInicial.gerar_sol_inicial_30_pas()
solutions = []
fronteira_pareto = []
conjunto_fronteiras = []

numbers = generate_numbers(20, 45, 86)

#solution.TECNICA_OTIMIZACAO = 'episilon_restrito'
solution.TECNICA_OTIMIZACAO = 'soma_ponderada'
tempo_execucao = time.time()
for _ in range(5):
    fronteira_pareto = []
    for i in range(20):
        init.RAIO_PA = numbers[i]
        init.iniciar_dados()
        solutions.append(vnd(solucao_inicial, len(VIZINHANCA)))
    
    conjunto_fronteiras.append(fronteira_pareto)

tempo_execucao = time.time() - tempo_execucao
print_resultados.print_fronteiras_pareto(conjunto_fronteiras)
print("tempo de execucao:",tempo_execucao)
# plotar resultados
# for solucao in solutions:
#     fitness = solution.get_solution(solucao[0])
#     print_resultados.print_solucao(fitness[0])
#     print_resultados.print_plano_cartesiano(fitness[0])
#     print_resultados.plot_pas(fitness[0])
#     print_resultados.plotar_resultados_otimizacao(solucao[1])