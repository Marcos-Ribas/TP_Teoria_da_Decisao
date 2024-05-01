# gerara_solucao.py

import numpy as np
import Iniciar_dados as init
from print_resultados import plot_pas

N_USERS = 495

def avaliar_fit(pas_solution):
    pas_utilizados = len(pas_solution)
    distancia_total = 0

    for pa in pas_solution:
        for user in pa.usuarios_atendidos:
            distancia_total += float(user.distancias_pas[pa.indice])

    return (pas_utilizados, distancia_total)

def criterio_parada(users):
    contador = 0
    for user in users:
        if user.user_atendido == True:
            contador += 1
    
    if contador/N_USERS >= 0.95:
        return True
    
    else:
        return False

def atribuir_users(pa, users, indice):
    pa_aux = pa
    pa_aux.usuarios_atendidos = []
    for user in users:
        if (float(user.distancias_pas[indice]) <= pa_aux.raio) and (pa_aux.banda_disponivel >= user.demandaRede) and (user.user_atendido == False):
            pa_aux.usuarios_atendidos.append(user)
            user.user_atendido = True
            pa_aux.banda_disponivel = pa_aux.banda_disponivel - user.demandaRede
            pa_aux.PA_ativado = True
            user.PA_conectado = pa_aux.coordenadas

        if pa_aux.banda_disponivel < 0.009:
            break

    return (pa_aux, users)

def pas_utilizados(pas):
    pas_utilizados = []
    for pa in pas:
        if pa.PA_ativado == True:
            pas_utilizados.append(pa)

    return pas_utilizados

def get_solution(vetor):    
    #print("Runing...")
    users = init.inicializar_users()
    pas = init.inicializar_PAs()
    indices = np.argsort(vetor)
    for i in indices:
        pas[i], users = atribuir_users(pas[i], users, i)
        if criterio_parada(users):
            break
    
    return pas_utilizados(pas), users