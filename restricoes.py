import math
import numpy as np
import Iniciar_dados as init

def calcular_exposicao(cliente, p_a):
    return (1 / math.dist((cliente.coordenadas), (p_a.coordenadas)))

def restricao_exposicao(p_as):
    users = init.inicializar_users()
    for user in users:
        if (np.sum([ calcular_exposicao(user, p_a) for p_a in p_as if p_a.PA_ativado]) >= 0.05):
            return False
    return True
    


