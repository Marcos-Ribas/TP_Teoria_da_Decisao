import matplotlib.pyplot as plt
import random

def print_user(users):
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
    for PA in solucao:
        user_atendidos = PA.usuarios_atendidos
        print("Usuários atendidos pelo PA:", PA.coordenadas, ":")
        for elemento in user_atendidos:
            print(elemento.coordenadas, end='')
            cont += 1
        
        print("\n",cont)
        cont = 0
        print(PA.banda_disponivel)


    
def print_plano_cartesiano(solucao):


    # Lista de vetores de pontos
    vetores = []
    coordenadas_PAs = []
    contador_users = 0

    for PA in solucao:
        user_atendidos = PA.usuarios_atendidos
        aux = []
        for elemento in user_atendidos:
            aux.append(elemento.coordenadas)
            contador_users+=1
        
        vetores.append(aux)
        coordenadas_PAs.append(PA.coordenadas)

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
        plt.scatter(x, y, color=cor, label=f'PA na posição {coordenadas_PAs[i]}')

    # Adicionar legenda
    plt.legend()

    plt.title(f'Número de user atendidos: {contador_users} \n número de PAs utilizados: {len(solucao)}')
    # Mostrar o gráfico 
    plt.show()