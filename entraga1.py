import numpy as np



MALHA_PAS = 40
BANDA_DISPONIVEL_PA = 54

class usuarios:
    
    coordenadas = ()
    distancias_pas = []
    PA_conectado = 0
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

    with open('distancias.csv', 'r') as file:
        i = 0
    # Iterando sobre cada linha do arquivo
        for line in file:
            # Dividindo a linha em partes usando a vírgula como separador
            parts = line.strip().split(',')
            users[i].distancias_pas = parts
            i+=1
    
    return users
        
            
def inicializar_PAs():
    PAs = []

    for i in range(MALHA_PAS):
        for j in range(MALHA_PAS):
            PAs.append(pontos_acesso((i,j)))

    return PAs

def inicializar_users():
    users =  []
    dados = ler_dados_csv()
    for dado in dados:
        users.append(usuarios(dado[0],dado[1]))
    
    users = atribuir_distancias(users)
    
    return users


users = inicializar_users()
PAs = inicializar_PAs()

for PA in PAs:
    print(PA.coordenadas)

