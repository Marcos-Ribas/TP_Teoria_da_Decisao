# print_resultados.py

import matplotlib.pyplot as plt
import random
import numpy as np

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
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

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
    
def plotar_graficos_distancias(dados):
    # Encontrar o comprimento máximo de todas as séries
    max_len = max(len(sublist) for sublist in dados)

    # Preparar os dados para plotagem
    menores_valores = []  # Lista para armazenar os menores valores de cada dataset

    for i, sublist in enumerate(dados):
        y = [tupla[1] for tupla in sublist]
        x = np.arange(1, max_len + 1)
        if len(sublist) < max_len:
            last_value = sublist[-1][1]
            y += [last_value] * (max_len - len(sublist))
        plt.plot(x, y, linestyle='-', label=f'Dataset {i+1}')
        
        # Encontrar o menor valor de cada dataset
        menor_valor = min(sublist, key=lambda x: x[1])[1]
        menores_valores.append(menor_valor)

    # Configurações do gráfico
    plt.title('Convergencia otimizacao distancias')
    plt.xlabel('Índice')
    plt.ylabel('Valores')
    plt.grid(True)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    # Calcular min, std e max dos menores valores
    menores_valores = np.array(menores_valores)
    print("Min:", np.min(menores_valores))
    print("Std:", np.std(menores_valores))
    print("Max:", np.max(menores_valores))
    
def plotar_graficos_numeros(dados):
    # Encontrar o comprimento máximo de todas as séries
    max_len = max(len(sublist) for sublist in dados)

    # Preparar os dados para plotagem
    menores_valores = []  # Lista para armazenar os menores valores de cada dataset

    for i, sublist in enumerate(dados):
        y = [tupla[0] for tupla in sublist]
        x = np.arange(1, max_len + 1)
        if len(sublist) < max_len:
            last_value = sublist[-1][0]
            y += [last_value] * (max_len - len(sublist))
        plt.plot(x, y, linestyle='-', label=f'Dataset {i+1}')
        
        # Encontrar o menor valor de cada dataset
        menor_valor = min(sublist, key=lambda x: x[0])[0]
        menores_valores.append(menor_valor)

    # Configurações do gráfico
    plt.title('Convergencia otimizacao numero pas')
    plt.xlabel('Índice')
    plt.ylabel('Valores')
    plt.grid(True)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    # Calcular min, std e max dos menores valores
    menores_valores = np.array(menores_valores)
    print("Min:", np.min(menores_valores))
    print("Std:", np.std(menores_valores))
    print("Max:", np.max(menores_valores))

def pareto_frontier(vetor):
    # Dicionário para armazenar o menor valor de y para cada x
    menores_valores = {}

    # Itera sobre a lista de tuplas
    for x, y in vetor:
        # Se x não estiver no dicionário ou y for menor que o valor atual de x no dicionário, atualiza o dicionário
        if x not in menores_valores or y < menores_valores[x]:
            menores_valores[x] = y

    # Converte o dicionário de volta para uma lista de tuplas
    vetor_reduzido = [(x, y) for x, y in menores_valores.items()]

    # Ordenar o vetor reduzido com base no primeiro valor da tupla (x)
    vetor_reduzido = sorted(vetor_reduzido, key=lambda x: x[0])
    
    # Inicializar a lista da fronteira de Pareto
    pareto_front = []
    
    # Variável para armazenar o menor valor de y encontrado até agora
    max_y = float('inf')
    
    # Iterar sobre o vetor reduzido
    for x, y in vetor_reduzido:
        # Verificar se a tupla (x, y) é não dominada
        if y < max_y:
            pareto_front.append((x, y))
            max_y = y

    return pareto_front

def print_fronteiras_pareto(fronteiras):
    # Combinar todas as fronteiras em uma única lista
    todas_solucoes = [ponto for fronteira in fronteiras for ponto in fronteira]
    
    # Determinar os limites dos eixos
    x_values = [x for x, y in todas_solucoes]
    y_values = [y for x, y in todas_solucoes]
    x_min, x_max = min(x_values) - 1, max(x_values) + 1
    y_min, y_max = min(y_values) - 1, max(y_values) + 1
    
    # Criando o gráfico
    plt.figure(figsize=(8, 6))

    # Calcular a fronteira de Pareto para todas as soluções combinadas
    fronteira_pareto = pareto_frontier(todas_solucoes)
    for x, y in fronteira_pareto:
        plt.scatter(x, y, color='red')

    # Adicionar título e rótulos
    plt.title('Plot of Tuples (x, y)')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.legend('Fronteira Pareto')

    # Mostrar o gráfico
    plt.grid(True)
    plt.show()
