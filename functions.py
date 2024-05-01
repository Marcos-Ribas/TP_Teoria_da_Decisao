# functions.py

import numpy as np
import random
from Gerar_solucao import avaliar_fit
from Gerar_solucao import get_solution

def neighborhood_change(solucao_atual, prox_solucao, k, objetivo_otimizacao = "ambos"):

    n_pas_atual, distancia_total_atual = avaliar_fit(get_solution(solucao_atual)[0])
    n_pas_prox, distancia_total_prox = avaliar_fit(get_solution(prox_solucao)[0])
    melhor_solucao = solucao_atual

    if(objetivo_otimizacao == "numero_pas"):

        if(n_pas_prox < n_pas_atual):
            melhor_solucao = prox_solucao
            print("solucao mudou")
            k = 1
        
        else:
            k = k+1

        return melhor_solucao, k
    
    elif(objetivo_otimizacao == "distancias"):
        if distancia_total_prox < distancia_total_atual:
            melhor_solucao = prox_solucao
            print("solucao mudou")
            k = 1
        else:
            k = k + 1

        return melhor_solucao, k
    
    else:

        if(n_pas_prox < n_pas_atual and distancia_total_prox < distancia_total_atual):
            melhor_solucao = prox_solucao
            print("solucao mudou")
            k = 1
        
        else:
            k = k+1

        return melhor_solucao, k


def shake(vetor_prioridades, k):
    if k == 1:
        vetor_ordenado = np.argsort(vetor_prioridades)
        direcao_troca = random.choice(["N","S","L","W"])
        posicao_troca = random.choice(vetor_ordenado[:5])
        
        if direcao_troca == "S" and posicao_troca-80 >= 0:
            vetor_prioridades[posicao_troca-80], vetor_prioridades[posicao_troca] = vetor_prioridades[posicao_troca], vetor_prioridades[posicao_troca-80]

        elif direcao_troca == "N" and posicao_troca+80 <= 1600:
            vetor_prioridades[posicao_troca+80], vetor_prioridades[posicao_troca] = vetor_prioridades[posicao_troca], vetor_prioridades[posicao_troca+80]

        elif direcao_troca == "L" and posicao_troca-1 >= 0:
            vetor_prioridades[posicao_troca-1], vetor_prioridades[posicao_troca] = vetor_prioridades[posicao_troca], vetor_prioridades[posicao_troca-1]


        elif direcao_troca == "W" and posicao_troca+1 <= 1600:
            vetor_prioridades[posicao_troca+1], vetor_prioridades[posicao_troca] = vetor_prioridades[posicao_troca], vetor_prioridades[posicao_troca+1]

    elif k == 2:
        for i in range (5):
            vetor_ordenado = np.argsort(vetor_prioridades)
            direcao_troca = random.choice(["N","S","L","W"])
            posicao_troca = random.choice(vetor_ordenado[:5])
            
            if direcao_troca == "S" and posicao_troca-80 >= 0:
                vetor_prioridades[posicao_troca-80], vetor_prioridades[posicao_troca] = vetor_prioridades[posicao_troca], vetor_prioridades[posicao_troca-80]

            elif direcao_troca == "N" and posicao_troca+80 <= 1600:
                vetor_prioridades[posicao_troca+80], vetor_prioridades[posicao_troca] = vetor_prioridades[posicao_troca], vetor_prioridades[posicao_troca+80]

            elif direcao_troca == "L" and posicao_troca-1 >= 0:
                vetor_prioridades[posicao_troca-1], vetor_prioridades[posicao_troca] = vetor_prioridades[posicao_troca], vetor_prioridades[posicao_troca-1]

            elif direcao_troca == "W" and posicao_troca+1 <= 1600:
                vetor_prioridades[posicao_troca+1], vetor_prioridades[posicao_troca] = vetor_prioridades[posicao_troca], vetor_prioridades[posicao_troca+1]

    elif k == 3:
        for i in range(20):
            vetor_ordenado = np.argsort(vetor_prioridades)
            posicao_troca1 = random.choice(vetor_ordenado[:5])
            posicao_troca2 = random.choice(vetor_ordenado)
            
            # Trocando os valores nas posições escolhidas
            vetor_prioridades[posicao_troca1], vetor_prioridades[posicao_troca2] = vetor_prioridades[posicao_troca2], vetor_prioridades[posicao_troca1]

    return vetor_prioridades

