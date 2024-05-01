# print_resultados.py

import matplotlib.pyplot as plt
import random

def plot_user(users):
    coordenadas = []

    for user in users:
        coordenadas.append(user.coordenadas)
    

    # Separando as coordenadas x e y das tuplas
    coordenadas_x = [tupla[0] for tupla in coordenadas]
    coordenadas_y = [tupla[1] for tupla in coordenadas]

    # Plotando as coordenadas no plano cartesiano
    plt.scatter(coordenadas_x, coordenadas_y, color='blue')

    # Adicionando título e rótulos aos eixos
    plt.title("Localização dos Usuários")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")

    # Exibindo o gráfico
    plt.grid(True)
    plt.show()

def print_solucao(solucao):
    cont = 0
    for pa in solucao:
        user_atendidos = pa.usuarios_atendidos
        print("Usuários atendidos pelo PA:", pa.coordenadas, ":")
        for elemento in user_atendidos:
            print(elemento.coordenadas, end='')
            cont += 1
        
        print("\n",cont)
        cont = 0
        print(pa.banda_disponivel)
        print("------------------------------")

    
def print_plano_cartesiano(solucao):


    # Lista de vetores de pontos
    vetores = []
    coordenadas_pas = []
    contador_users = 0

    for pa in solucao:
        user_atendidos = pa.usuarios_atendidos
        aux = []
        for elemento in user_atendidos:
            aux.append(elemento.coordenadas)
            contador_users+=1
        
        vetores.append(aux)
        coordenadas_pas.append(pa.coordenadas)

    # Cores disponíveis para plotagem
    import matplotlib.colors as mcolors

    all_colors = list(mcolors.CSS4_COLORS.items())

    # Filtrar cores com luminosidade menor que 0.5 (cores mais escuras)
    cores = [cor for cor, rgb in all_colors if mcolors.rgb_to_hsv(mcolors.to_rgb(rgb))[2] < 0.75]

    # Iterar sobre cada vetor e plotar
    for i, pontos in enumerate(vetores):
        # Gerar uma cor aleatória para cada vetor
        cor = cores[i]
        
        # Extrair coordenadas x e y do vetor
        x, y = zip(*pontos)
        
        # Plotar os pontos com a cor selecionada
        plt.scatter(x, y, color=cor, label=f'PA na posição {coordenadas_pas[i]}')

    # Adicionar legenda
    plt.legend()

    plt.title(f'Número de user atendidos: {contador_users} \n número de PAs utilizados: {len(solucao)}')
    # Mostrar o gráfico 
    plt.show()

def print_user(users):
    for user in users:
        print(user.coordenadas, " ", user.user_atendido)

def plot_pas(pas):
    coordenadas = []

    for pa in pas:
        coordenadas.append(pa.coordenadas)
    

    # Separando as coordenadas x e y das tuplas
    coordenadas_x = [tupla[0] for tupla in coordenadas]
    coordenadas_y = [tupla[1] for tupla in coordenadas]

    # Plotando as coordenadas no plano cartesiano
    plt.scatter(coordenadas_x, coordenadas_y, color='blue')

    # Adicionando título e rótulos aos eixos
    plt.title("Localização dos PAs")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")

    # Exibindo o gráfico
    plt.grid(True)
    plt.show()

# Função para plotar os resultados da otimização
def plotar_resultados_otimizacao(avaliacoes):
    numero_pas = [tupla[0] for tupla in avaliacoes]
    distancia = [tupla[1] for tupla in avaliacoes]
    # Número total de iterações
    num_iteracoes = len(avaliacoes)
    # Criar uma lista de iterações sequenciais
    iteracoes = list(range(1, num_iteracoes + 1))

    # Configurações do gráfico
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.set_xlabel('Iteração')
    ax1.set_ylabel('Distâncias', color='b')
    ax1.plot(iteracoes, distancia, marker='o', linestyle='-', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.set_ylabel('PAs utilizados', color='r')
    ax2.plot(iteracoes, numero_pas, marker='o', linestyle='-', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    plt.title('Evolução da solução para o número de PAs e distâncias')

    # Exibir o gráfico
    plt.show()