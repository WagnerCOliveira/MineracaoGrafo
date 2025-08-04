import multiprocessing
import networkx as nx  
import random
import time


def media_distancias_entre_pares(lcc_):
    """Média das Distâncias entre Pares"""

    if nx.is_connected(lcc_):        
        print("A rede é conectada.")
        avg_path_length_estimate = nx.average_shortest_path_length(lcc_)   
        return print(f"Média das Distâncias entre Pares: {avg_path_length_estimate:.2f} passos")  
    else:  
        print("A rede é desconectada.")        
        componentes = nx.connected_components(lcc_)
        maior_comp_nodes = max(componentes, key=len)
        
        print('Cria um subgrafo com o MAX correspondente para analise')
        componente_maior = lcc_.subgraph(maior_comp_nodes).copy()
        
        print(f"Novo subgrafo criado com {componente_maior.number_of_nodes()} nós e {componente_maior.number_of_edges()} arestas.")
        avg_path_length_estimate = nx.average_shortest_path_length(componente_maior)
        return print(f"Média das Distâncias entre Pares: {avg_path_length_estimate:.2f} passos")
     


if __name__ == '__main__':
    
    G = nx.read_edgelist('datasets/phonecalls.edgelist.txt')    
    
    lcc_nodes = list(max(nx.connected_components(G), key=len)) 

    # 3. Criar o subgrafo a partir da lista de nós
    LCC_subgraph = G.subgraph(lcc_nodes).copy() # Usar .copy() para ter um grafo independente

    print(f"Número de nós no grafo original (G): {G.number_of_nodes()}")
    print(f"Número de nós no Maior Componente Conectado (LCC): {LCC_subgraph.number_of_nodes()}")
    print("-" * 30)


    ### PASSO 2: Amostrar 20% dos Nós do LCC

    # Pega a lista de todos os nós que estão no LCC
    lcc_node_list = list(LCC_subgraph.nodes())

    # Calcula quantos nós correspondem a 20% do LCC
    # Usamos int() para garantir que o resultado seja um número inteiro
    num_nodes_to_sample = int(LCC_subgraph.number_of_nodes() * 0.05)

    # Seleciona aleatoriamente 'num_nodes_to_sample' nós da lista, sem reposição
    sampled_nodes = random.sample(lcc_node_list, k=num_nodes_to_sample)

    print(f"Vamos amostrar 20% do LCC, o que corresponde a {num_nodes_to_sample} nós.")
    # print(f"Nós amostrados: {sampled_nodes}") # Descomente para ver os nós
    print("-" * 30)

    ### PASSO 3: Criar o Subgrafo Final com os 20% dos Nós

    # Cria o subgrafo final a partir do LCC, usando apenas os nós amostrados
    # Este novo grafo conterá os nós amostrados e TODAS as arestas que existiam ENTRE ELES no LCC
    LCC_20_percent = LCC_subgraph.subgraph(sampled_nodes).copy()

    print(f"Novo subgrafo criado com {LCC_20_percent.number_of_nodes()} nós e {LCC_20_percent.number_of_edges()} arestas.")

    lcc_ = nx.subgraph(G, lcc_nodes)

    # Cria um pool com o número de processos disponíveis na máquina
    inicio_par = time.time()
    
    media_distancias_entre_pares(lcc_)
    fim_par = time.time()
    print(f"Tempo de execução paralela: {(fim_par - inicio_par)/60:.4f} minutos")