import numpy as np
import random
import print_resultados
import Iniciar_dados as init
import Gerar_solucao as solution
import functions as func
import copy
    
    
def VND(X, Kmax):
    fitness_evolution = []
    k = 1
    print(solution.avaliar_fit(solution.get_solution(X)[0]))

    while(k <= Kmax):
        print("K = ", k)
        vetor_solucoes = []
        vetor_prioridades = []

        for i in range(10):
            vetor_prioridades.append(copy.deepcopy(func.shake(list(X), k)))
            vetor_solucoes.append(solution.avaliar_fit(solution.get_solution(vetor_prioridades[i])[0]))

        indice = min(enumerate(vetor_solucoes), key=lambda x: x[1][0])[0]
        X_linha = vetor_prioridades[indice]
        
        X, k = func.Neighborhood_change(X, X_linha, k)
        fitness_evolution.append(solution.avaliar_fit(solution.get_solution(X)[0]))
        print(solution.avaliar_fit(solution.get_solution(X)[0]))

    return X, fitness_evolution



vetor_prioridades = np.random.permutation(6400)

solucao = VND(vetor_prioridades, 3)

fitness = solution.get_solution(solucao[0])

print_resultados.print_solucao(fitness[0])
print_resultados.print_plano_cartesiano(fitness[0])
print_resultados.plot_PAs(fitness[0])
print(solucao[1])



