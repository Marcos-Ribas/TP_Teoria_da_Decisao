import matplotlib.pyplot as plt

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