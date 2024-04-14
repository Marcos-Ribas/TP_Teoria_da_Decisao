coordenadas = []
demanda = []

dados = []

import numpy as np

def distancia_euclidiana_entre_tuplas(tupla1, tupla2):
    """
    Calcula a distância euclidiana entre duas tuplas.

    Args:
    tupla1 (tuple): A primeira tupla de coordenadas.
    tupla2 (tuple): A segunda tupla de coordenadas.

    Returns:
    float: A distância euclidiana entre as duas tuplas.
    """
    # Convertendo as tuplas em arrays numpy para facilitar os cálculos
    coord1 = np.array(tupla1)
    coord2 = np.array(tupla2)

    # Calculando a diferença entre as coordenadas de cada dimensão
    diferenca = coord2 - coord1

    # Calculando o quadrado da diferença
    quadrado_diferenca = diferenca ** 2

    # Somando os quadrados das diferenças em cada dimensão
    soma_quadrados = np.sum(quadrado_diferenca)

    # Calculando a raiz quadrada da soma dos quadrados das diferenças
    distancia = np.sqrt(soma_quadrados)

    return distancia

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
            
            dados.append((coordenadas))

PAs = []

for i in range(80):
    for j in range(80):
        PAs.append((i*5,j*5))

distancias = []

for dado in dados:
    cont = 0
    A = []
    for PA in PAs:
        A.append(distancia_euclidiana_entre_tuplas(dado,PA))
        cont+=1
    
    distancias.append(A)

nome_arquivo = 'distancias.txt'

# Abrir o arquivo de texto em modo de escrita
with open(nome_arquivo, 'w') as arquivo_txt:
    # Iterar sobre cada vetor no vetor de vetores
    for vetor in distancias:
        # Converter os elementos do vetor para strings e juntá-los em uma única linha
        linha = ' '.join(map(str, vetor)) + '\n'
        # Escrever a linha no arquivo de texto
        arquivo_txt.write(linha)

print("Arquivo de texto foi criado com sucesso.")
