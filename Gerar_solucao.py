import numpy as np
import Iniciar_dados as init
from print_resultados import plot_PAs

N_USERS = 495

def avaliar_fit(PAs_solution):
    PAs_utilizados = len(PAs_solution)
    distancia_total = 0

    for PA in PAs_solution:
        for user in PA.usuarios_atendidos:
            distancia_total += float(user.distancias_pas[PA.indice])

    return (PAs_utilizados, distancia_total)



def criterio_parada(users):
    contador = 0
    for user in users:
        if user.user_atendido == True:
            contador += 1
    
    if contador/N_USERS >= 0.95:
        return True
    
    else:
        return False

def atribuir_users(PA, users, indice):
    PA_aux = PA
    PA_aux.usuarios_atendidos = []
    for user in users:
        var = float(user.distancias_pas[indice])
        if (float(user.distancias_pas[indice]) <= PA_aux.raio) and (PA_aux.banda_disponivel >= user.demandaRede) and (user.user_atendido == False):
            PA_aux.usuarios_atendidos.append(user)
            user.user_atendido = True
            PA_aux.banda_disponivel = PA_aux.banda_disponivel - user.demandaRede
            PA_aux.PA_ativado = True
            user.PA_conectado = PA_aux.coordenadas

        if PA_aux.banda_disponivel < 0.009:
            break
        
        pass

    return (PA_aux, users)

def PAs_utilizados(PAs):
    count = 0
    PAs_utilizados = []
    for PA in PAs:
        if PA.PA_ativado == True:
            count += 1
            PAs_utilizados.append(PA)

    return PAs_utilizados

def get_solution(vetor):    
    print("Runing...")
    users = init.inicializar_users()
    PAs = init.inicializar_PAs()
    indices = np.argsort(vetor)
    for i in indices:
        PAs[i], users = atribuir_users(PAs[i], users, i)
        if criterio_parada(users):
            break
    
    return PAs_utilizados(PAs), users