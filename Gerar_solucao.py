# gerara_solucao.py

import numpy as np
import Iniciar_dados as init
import copy
import restricoes


MAXIMO_PAS = 30
N_USERS = 495
TECNICA_OTIMIZACAO = 'episilon_restrito'

peso_nPAs = 1
PESO_Distancias = 1

def avaliar_fit(pas_solution):
    
    pas_utilizados = len(pas_solution)
    distancia_total = 0
    cont = 0
    
    for pa in pas_solution:
        pa.total_distance = sum(float(user.distancias_pas[pa.indice]) for user in pa.usuarios_atendidos)
        distancia_total += pa.total_distance
    penalidade = 0
    if cont > MAXIMO_PAS or restricoes.restricao_exposicao(pas_solution):
        penalidade = cont - MAXIMO_PAS

    if TECNICA_OTIMIZACAO == 'episilon_restrito':
        return (pas_utilizados, distancia_total + penalidade*1000)
    
    elif TECNICA_OTIMIZACAO == 'soma_ponderada':

        pas_utilizados_normalized, distancias_nomalized = normalize(pas_utilizados, distancia_total + penalidade*1000)

        fit = peso_nPAs*pas_utilizados_normalized + PESO_Distancias*distancias_nomalized

        return (pas_utilizados, distancia_total + penalidade*1000, fit)
    pass

def normalize(x, y):
    # Normaliza a variável x que varia de 0 a 30
    x_min = 0
    x_max = 30
    x_normalized = (x - x_min) / (x_max - x_min)

    # Normaliza a variável y que varia de 0 a 25000
    y_min = 0
    y_max = 25000
    y_normalized = (y - y_min) / (y_max - y_min)

    return x_normalized, y_normalized

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
    total_distance = 0
    for user in users:
        if (float(user.distancias_pas[indice]) <= pa_aux.raio) and (pa_aux.banda_disponivel >= user.demandaRede) and (user.user_atendido == False):
            pa_aux.usuarios_atendidos.append(user)
            user.user_atendido = True
            pa_aux.banda_disponivel = pa_aux.banda_disponivel - user.demandaRede
            pa_aux.PA_ativado = True
            user.PA_conectado = pa_aux.coordenadas
            total_distance += float(user.distancias_pas[indice])

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
    users = [copy.copy(user) for user in init.Users]
    pas = [copy.copy(pa) for pa in init.PAs]
    indices = np.argsort(vetor)
    for i in indices:
        pas[i], users = atribuir_users(pas[i], users, i)
        if criterio_parada(users):
            break
    
    return pas_utilizados(pas), users