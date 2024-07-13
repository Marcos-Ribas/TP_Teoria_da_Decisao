import numpy as np
from sklearn.cluster import KMeans
import skfuzzy as fuzz
import matplotlib.pyplot as plt

def gerar_sol_inicial(objetivo = 'numero_pas'):
    # Load data from file
    dados = np.loadtxt('clientes.txt', delimiter=',')

    # Extract X and Y coordinates
    X = dados[:, 0]
    Y = dados[:, 1]

    dados2 =  [(x[0], x[1]) for x in dados]

    # Plot the scatter plot
    #plt.figure(figsize=(8, 6))
    #plt.scatter(X, Y, color='blue')
    #plt.title('Diagrama de Dispersão: coordenadas X e Y')
    #plt.xlabel('X')
    #plt.ylabel('Y')
    #plt.grid(True)
    #plt.show()

    # Apply K-Means algorithm
    kmeans = KMeans(n_clusters=10)
    kmeans.fit(dados2)
    Clusters_kMeans = kmeans.predict(dados2)
    Centroids_kMeans = kmeans.cluster_centers_

    # Visualize the results
    #plt.scatter(dados[:, 0], dados[:, 1], c=Clusters_kMeans, cmap='viridis', alpha=0.5, label='Dados')
    #plt.scatter(Centroids_kMeans[:, 0], Centroids_kMeans[:, 1], c='red', marker='x', label='Centroids')
    #plt.title('Resultados do K-Means')
    #plt.xlabel('Feature 1')
    #plt.ylabel('Feature 2')
    #plt.legend()
    #plt.show()

    # Convert dados2 to a 2D array
    dados2_array = np.array(dados2)

    # Apply Fuzzy C-Means algorithm
    if objetivo == 'numero_pas':
        Centroids_FCM, U_FCM, _, _, _, _, _ = fuzz.cluster.cmeans(dados2_array.T, 10, 2.0, error=0.005, maxiter=1000)

    if objetivo == 'distancias':
        Centroids_FCM, U_FCM, _, _, _, _, _ = fuzz.cluster.cmeans(dados2_array.T, 30, 2.0, error=0.005, maxiter=1000)
    
    Clusters_FCM = np.argmax(U_FCM, axis=0)

    # Visualize the results of FCM
    #plt.scatter(dados[:, 0], dados[:, 1], c=Clusters_FCM, cmap='viridis', alpha=0.5, label='Dados')
    #plt.scatter(Centroids_FCM[:, 0], Centroids_FCM[:, 1], c='red', marker='x', label='Centroids')
    #plt.title('Resultados do C-Means')
    #plt.xlabel('Feature 1')
    #plt.ylabel('Feature 2')
    #plt.legend()
    plt.show()

    centroides_arredondadas = np.round(Centroids_FCM / 5) * 5

    posicoes = []
    for x in centroides_arredondadas:
        posicoes.append(int((x[0]/5)*80 + (x[1]/5)))

    #print(posicoes)

    vetor_prioridades = np.random.permutation(6400)
    #print(vetor_prioridades)
    i=0
    for elemento in posicoes:
        indice = np.where(vetor_prioridades == i)
        aux = vetor_prioridades[elemento]
        vetor_prioridades[elemento] = i
        vetor_prioridades[indice] = aux
        i+=1

    return vetor_prioridades

    #print(vetor_prioridades)

def gerar_sol_inicial_30_pas():
    # Carregar dados do arquivo
    dados = np.loadtxt('clientes.txt', delimiter=',')

    # Extrair coordenadas X, Y e demandas
    X = dados[:, 0]
    Y = dados[:, 1]
    demands = dados[:, 2]

    dados2 = np.column_stack((X, Y, demands))

    # Aplicar algoritmo K-Means para encontrar 30 clusters, ponderados pelas demandas
    kmeans = KMeans(n_clusters=30)
    kmeans.fit(dados2, sample_weight=demands)
    centroids_kmeans = kmeans.cluster_centers_

    # Arredondar centroides para o múltiplo mais próximo de 5
    centroides_arredondadas = np.round(centroids_kmeans[:, :2] / 5) * 5

    # Mapear centroides para posições na grade
    posicoes = []
    for x in centroides_arredondadas:
        posicoes.append(int((x[0] / 5) * 80 + (x[1] / 5)))

    vetor_prioridades = np.random.permutation(6400)
    i = 0
    for elemento in posicoes:
        indice = np.where(vetor_prioridades == i)
        aux = vetor_prioridades[elemento]
        vetor_prioridades[elemento] = i
        vetor_prioridades[indice] = aux
        i += 1
    
    #plt.figure(figsize=(10, 8))
    #plt.scatter(X, Y, c='blue', label='Clientes')
    #plt.scatter(centroids_kmeans[:, 0], centroids_kmeans[:, 1], c='red', marker='x', label='Centroides')

    #plt.title('Bacias de Atração dos Centroides')
    #plt.xlabel('Coordenada X')
    #plt.ylabel('Coordenada Y')
    #plt.legend()
    #plt.grid(True)
    #plt.show()

    return vetor_prioridades