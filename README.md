README
Descrição
Este código é uma implementação de um algoritmo de otimização para atribuição de usuários em pontos de acesso (PAs) em uma malha de comunicação. Ele visa otimizar a utilização dos recursos de banda disponível em cada PA, enquanto atende à demanda dos usuários e mantém uma boa cobertura da área de serviço.

Funcionalidades
Inicializa usuários e pontos de acesso com coordenadas e características específicas.
Lê dados de entrada de um arquivo CSV contendo as coordenadas dos usuários e suas demandas de banda.
Calcula as distâncias entre cada usuário e todos os pontos de acesso usando um arquivo de distâncias pré-computadas.
Atribui os usuários aos pontos de acesso de acordo com critérios de otimização, garantindo que as demandas de banda sejam atendidas e que a cobertura da área seja mantida.
Verifica um critério de parada para determinar quando a solução é satisfatória.
Gera resultados e visualizações, incluindo a quantidade de PAs utilizados, a lista de usuários atribuídos a cada PA e um plano cartesiano mostrando a distribuição dos usuários e dos PAs na malha.
Pré-requisitos
Python 3.x
Bibliotecas: numpy, matplotlib (para visualizações)
Utilização
Certifique-se de ter os dados dos clientes em um arquivo CSV chamado clientes.csv.
Certifique-se de ter as distâncias pré-computadas em um arquivo de texto chamado distancias.txt.
Execute o script print_resultados.py para definir a função de visualização dos resultados.
Execute o script principal para obter a solução do problema de otimização e visualizar os resultados.
Observações
Certifique-se de ajustar os parâmetros do problema, como tamanho da malha, banda disponível nos PAs e raio de cobertura dos PAs, conforme necessário.
Os arquivos CSV e de texto devem estar formatados corretamente para garantir o funcionamento adequado do código.
