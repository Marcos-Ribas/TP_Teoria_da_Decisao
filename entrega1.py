import numpy as np
import print_resultados

MALHA_PAS = 80
BANDA_DISPONIVEL_PA = 54
RAIO_PA = 85
N_USERS = 495

class usuarios:
    
    coordenadas = ()
    distancias_pas = []
    PA_conectado = ()
    user_atendido = False
    demandaRede = 0

    def __init__(self, coordenadas = (0,0), demanda = 0):
        self.coordenadas = coordenadas
        self.demandaRede = demanda




class pontos_acesso:

    coordenadas = ()
    usuarios_atendidos = []
    banda_disponivel = BANDA_DISPONIVEL_PA
    PA_ativado = False
    raio = RAIO_PA

    def __init__(self, coordenadas):
        self.coordenadas = coordenadas


def ler_dados_csv():

    coordenadas = []
    demanda = []
    dados = []

    with open('clientes.csv', 'r') as file:
    # Iterando sobre cada linha do arquivo
        for line in file:
            # Dividindo a linha em partes usando a vírgula como separador
            parts = line.strip().split(',')
            
            # Verificando se existem exatamente três partes
            if len(parts) == 3:
                # Armazenando as duas primeiras partes em uma tupla
                coordenadas = (float(parts[0]), float(parts[1]))
                
                # Armazenando a terceira parte em uma variável
                demanda = float(parts[2])
                
                dados.append((coordenadas,demanda))

    return dados

def atribuir_distancias(users):

    with open('distancias.txt', 'r') as file:
        i = 0
    # Iterando sobre cada linha do arquivo
        for line in file:
            # Dividindo a linha em partes usando a vírgula como separador
            parts = line.strip().split(' ')
            users[i].distancias_pas = parts
            i+=1
    
    return users
        
            
def inicializar_PAs():
    PAs = []

    for i in range(MALHA_PAS):
        for j in range(MALHA_PAS):
            PAs.append(pontos_acesso((i*5,j*5)))

    return PAs

def inicializar_users():
    users =  []
    dados = ler_dados_csv()
    for dado in dados:
        users.append(usuarios(dado[0],dado[1]))
    
    users = atribuir_distancias(users)
    
    return users

def atribuir_users(PA, users, indice):
    PA_aux = PA
    PA_aux.usuarios_atendidos = []
    for user in users:
        var = float(user.distancias_pas[indice])
        if (float(user.distancias_pas[indice]) <= RAIO_PA) and (PA_aux.banda_disponivel >= user.demandaRede) and (user.user_atendido == False):
            PA_aux.usuarios_atendidos.append(user)
            user.user_atendido = True
            PA_aux.banda_disponivel = PA_aux.banda_disponivel - user.demandaRede
            PA_aux.PA_ativado = True
            user.PA_conectado = PA_aux.coordenadas

        if PA_aux.banda_disponivel < 0.009:
            break
        
        pass

    return (PA_aux, users)

def criterio_parada(users):
    contador = 0
    for user in users:
        if user.user_atendido == True:
            contador += 1
    
    if contador/N_USERS >= 0.95:
        return True
    
    else:
        return False

def PAs_utilizados(PAs):
    count = 0
    PAs_utilizados = []
    for PA in PAs:
        if PA.PA_ativado == True:
            count += 1
            PAs_utilizados.append(PA)
    
    print("foram utilizados, ", count, " PAs para a solução.")
    return PAs_utilizados

def get_solution(vetor, PAs, users):
    indices = np.argsort(vetor)
    print(len(indices), len(vetor))
    for i in indices:
        PAs[i], users = atribuir_users(PAs[i], users, i)
        if criterio_parada(users):
            print("criterio de parada atingido")
            break
    
    return PAs_utilizados(PAs), users

users = inicializar_users()
PAs = inicializar_PAs()

solucao = np.random.permutation(6400)

PAs_solution, user_solution = get_solution(solucao, PAs, users)

print_resultados.print_user(users)
print_resultados.print_solucao(PAs_solution)
print_resultados.print_plano_cartesiano(PAs_solution)




