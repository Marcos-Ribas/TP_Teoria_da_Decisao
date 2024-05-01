# leitura_CSV.py

import numpy as np
import math

def ler_dados_clientes_csv():
    # Carregando os dados do arquivo CSV
    data = np.genfromtxt('clientes.csv', delimiter=',')

    temp = []
    # Separando as coordenadas x e y
    for i in range(0,len(data)):
        temp.append({"coordenadas":(data[i,0],data[i,1]), "demanda":data[i,2]})
    
    return temp


def preencher_grid_distancias(dados):

    pas_disponiveis = []
    # preencher o grid de 400x400 com passo de 5
    for i in range(80):
        for j in range(80):
            pas_disponiveis.append((i*5,j*5))

    distancias = [[math.dist(dado["coordenadas"], PA) for PA in pas_disponiveis] for dado in dados]

    nome_arquivo = 'distancias.txt'

    np.savetxt(nome_arquivo, distancias)


preencher_grid_distancias(ler_dados_clientes_csv())