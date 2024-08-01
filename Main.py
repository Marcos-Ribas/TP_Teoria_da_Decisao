import numpy as np
import random
import print_resultados
import Iniciar_dados as init
import Gerar_solucao as solution
import functions as func
import copy
import solucaoInicial
import time
import export_to_json

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
    solucoes_objs = []
    fitness_evolution = []
    k = 1
    current_solution, current_users = solution.get_solution(x)
    current_fitness = solution.avaliar_fit(current_solution)
    print(current_fitness)

    while k <= k_max:
        print("K =", k)
        vetor_solucoes = []
        vetor_prioridades = []

        # Generate neighborhood solutions
        for i in range(30):
            priority_list = copy.deepcopy(func.shake(list(x), VIZINHANCA[2], OBJETIVO_OTIMIZACAO))
            vetor_prioridades.append(priority_list)
            solution_candidate, users_candidate = solution.get_solution(priority_list)
            fitness_candidate = solution.avaliar_fit(solution_candidate)
            vetor_solucoes.append((priority_list, fitness_candidate, solution_candidate))

        # Find the best solution in the neighborhood
        best_priority_list, best_fitness, best_solution = min(vetor_solucoes, key=lambda item: item[1][0])
        
        if best_fitness[0] < current_fitness[0]:
            x = best_priority_list
            current_solution = best_solution
            current_fitness = best_fitness
            k = 1
        else:
            k += 1

        fitness_evolution.append(current_fitness)
    
    solucoes_objs.append((current_solution, current_users, current_fitness[:2]))
    fronteira_pareto.append(current_fitness[:2])
    return x, fitness_evolution, solucoes_objs




solucao_inicial = solucaoInicial.gerar_sol_inicial_30_pas()
solutions = []
fronteira_pareto = []
conjunto_fronteiras = []

numbers = generate_numbers(20, 45, 86)

#solution.TECNICA_OTIMIZACAO = 'episilon_restrito'
solution.TECNICA_OTIMIZACAO = 'soma_ponderada'
tempo_execucao = time.time()
solucoes_objs = []
for _ in range(20):
    fronteira_pareto = []
    for i in range(20):
        init.RAIO_PA = numbers[i]
        init.iniciar_dados()
        x, y, objs = vnd(solucao_inicial, len(VIZINHANCA))
        solutions.append((x, y))
        solucoes_objs.append(objs)
    
    conjunto_fronteiras.append(fronteira_pareto)
tempo_execucao = time.time() - tempo_execucao
print_resultados.print_fronteiras_pareto(conjunto_fronteiras)
print("tempo de execucao:",tempo_execucao)
export_to_json.export_solutions_to_json(solucoes_objs)
export_to_json.export_pareto_to_json(solucoes_objs)
# plotar resultados
# for solucao in solutions:
#     fitness = solution.get_solution(solucao[0])
#     print_resultados.print_solucao(fitness[0])
#     print_resultados.print_plano_cartesiano(fitness[0])
#     print_resultados.plot_pas(fitness[0])
#     print_resultados.plotar_resultados_otimizacao(solucao[1])