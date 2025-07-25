

Tabela de conteúdos
---
<!--ts-->   
   * [Tecnologias](#🛠-tecnologias-utilizadas)
   * [Criação Virtualenv](#criação-virtualenv)
   * [Instalação Pacotes](#instalação-de-pacotes)
   * [Acessando Virtualenv](#acessando-virtualenv---wsl-linux)
   * [Baixando e Descompactador de Arquivos](#baixando-e-descompactador-de-arquivos)
   * [Atividade 1 - Disciplina de Mineração em Grafo](#atividade-1---disciplina-de-mineração-em-grafo)
   * [Estatística Descritiva de Redes Empíricas Utilizando NetworkX](#análise-estatística-descritiva-de-redes-empíricas-utilizando-networkx)
   * [Referências](#referências)
   * [Contribuição](#contribuição)
   * [Autor](#autor)
   * [Licença](#licença)
<!--te-->


Tecnologias Utilizadas
---
As seguintes ferramentas foram usadas na construção do projeto:

- [Python 3.13.0](https://docs.python.org/pt-br/3/)
- [networkx](https://networkx.org/documentation/stable/reference/index.html)
- [matplotlib](https://matplotlib.org/stable/index.html)
- [numpy](https://numpy.org/doc/)
- [Jupter Notebook](https://docs.jupyter.org/en/latest/)
- [nx-cugraph-cu12](https://pypi.org/project/nx-cugraph-cu12/)
- [tqdm](https://tqdm.github.io/)


Criação Virtualenv
---


~~~bash
python3 -m venv .venv
~~~


Acessando Virtualenv - WSL, Linux
---


~~~bash
source .venv/bin/activate
~~~


Acessando Virtualenv - Windows
---


~~~bash
.venv/Scripts/activate.bat
~~~


Instalação de Pacotes
---


~~~bash
python -m pip install -r requirements.txt
~~~


Baixando e Descompactador de Arquivos
---

Este é um script simples em Python feito para baixar um arquivo .zip de uma URL, mostrar uma barrinha de progresso, descompactar o conteúdo em uma pasta e, por fim, apagar o arquivo .zip que foi baixado.

### **Como Funciona?**

O script realiza os seguintes passos:

1. **Verifica a URL:** Ele pega a URL do arquivo que você quer baixar.  
2. **Cria a Pasta:** Se a pasta de destino (por padrão, datasets) não existir, o script a cria para você.  
3. **Baixa o Arquivo:** Ele inicia o download do arquivo e mostra uma barra de progresso para você acompanhar o andamento.  
4. **Descompacta Tudo:** Assim que o download termina, ele extrai todos os arquivos de dentro do .zip para a pasta de destino.  
5. **Limpa a Bagunça:** Para não deixar arquivos desnecessários ocupando espaço, ele remove o arquivo .zip original.


### **Como Usar**

1. O código do arquivo downloader_datasets.py.  


~~~Python
main:  
   def main():  
       # Altere a URL aqui se precisar  
       url_arquivo = 'https://networksciencebook.com/translations/en/resources/networks.zip'

       # Altere o nome da pasta de destino aqui se quiser  
       nome_diretorio = 'datasets'      

       try:  
           baixar_arquivo(url_arquivo, nome_diretorio)  
       except Exception as e:  
           print(f"Erro ao baixar ou descompactar arquivo: {e}")

~~~

2. è só executar o script pelo terminal:  

~~~bash
   python downloader_datasets.py
~~~

E pronto\! O script fará todo o trabalho para você. Se algo der errado, ele mostrará uma mensagem de erro.


Atividade 1 - Disciplina de Mineração em Grafo
---

### 12 de Julho 2025
### Prof. Hygor Piaget M. Melo 

Fazer o download do conjunto de redes empiricas https://networksciencebook.com/translations/en/resources/data.html

### Realizar uma análise de estatística descritiva nas 10 redes empíricas. Apresentar em um relatório no dia 25 de Julho 2025 e discutido durante a aula. 

* A estatística descritiva deve contar com pelo menos:
  * Tamanho da rede;
  * Número de links;
  * Grau médio;
  * Distribuição de graus;
  * Média das distâncias entre pares: 
    * Distância média entre todos os pares de nós na rede.
  * Diâmetro: 
    * A maior distância entre todos os pares de nós na rede, representando o tamanho geral da rede.


Análise Estatística Descritiva de Redes Empíricas Utilizando NetworkX
---


### **I. Introdução**

O objetivo principal realizar uma análise estatística descritiva abrangente de uma rede empírica, utilizando a biblioteca NetworkX em Python. A análise visa caracterizar as propriedades estruturais da rede para inferir sua eficiência, robustez e potencial para o fluxo de informações. Serão calculadas e interpretadas métricas específicas da rede, incluindo o tamanho da rede (número de nós), o número de links (arestas), o grau médio, a distribuição de graus, a média das distâncias entre pares e o diâmetro da rede.

### **II. Metodologia: Carregamento e Representação da Rede**

O ponto de partida para qualquer análise de rede empírica é o carregamento dos dados da rede em um objeto de grafo NetworkX. Esta etapa é crucial, pois a representação correta da estrutura da rede é fundamental para a precisão das análises subsequentes. O NetworkX oferece flexibilidade para ler dados de diversos formatos comuns de rede, como listas de arestas, listas de adjacências.

~~~Python

import networkx as nx  

G = nx.read_edgelist('datasets/actor.edgelist.txt')

~~~

### **III. Métricas Descritivas da Rede e Análise**

As métricas descritivas fornecem um panorama quantitativo das características estruturais de uma rede. A Tabela 1 oferece um resumo das métricas que serão detalhadas nas seções seguintes.

**Tabela 1: Resumo das Métricas Descritivas da Rede**

| Métrica | Valor Calculado | Unidade | Breve Descrição/Interpretação |
| :---- | :---- | :---- | :---- |
| Tamanho da Rede | N | nós | Escala total do sistema |
| Número de Links | M | links | Conectividade total da rede |
| Grau Médio | Z | passos | Conectividade média por nó |
| Média das Distâncias entre Pares | X | passos | Eficiência média de comunicação/transporte |
| Diâmetro da Rede | D | passos | Máxima separação entre dois nós; potencial de gargalos |

### **A. Tamanho da Rede (Número de Nós)**

O tamanho da rede, representado pelo número de nós (ou vértices), N, é a medida mais fundamental da escala de um sistema de rede. Ele quantifica o total de entidades ou atores individuais presentes na rede em estudo.

O NetworkX oferece funções diretas para obter o número de nós: G.number\_of\_nodes() ou, de forma mais concisa, len(G). Para a rede empírica analisada, assume-se que possui

N nós.

~~~Python

num_nodes = G.number_of_nodes()  
print(f"Tamanho da Rede (Número de Nós): {num_nodes} nós")
~~~

A escala da rede tem implicações diretas na viabilidade e na escolha dos métodos analíticos. Redes com um número muito grande de nós, como as redes sociais globais, podem tornar cálculos exatos para certas métricas, como os caminhos mais curtos ou o diâmetro, computacionalmente proibitivos. Nesses cenários, torna-se necessário empregar algoritmos de aproximação, como os disponíveis para o diâmetro , ou estratégias de amostragem. A escolha entre métodos exatos e aproximados envolve uma ponderação entre a precisão dos resultados e os recursos computacionais disponíveis.

### **B. Número de Links (Arestas)**

O número de links (ou arestas/laços), M, representa a contagem total de conexões ou relacionamentos entre os nós na rede. Esta métrica quantifica o nível geral de interação ou conectividade dentro do sistema.

O NetworkX fornece a função G.number\_of\_edges() para obter o número total de arestas. Alternativamente, o método G.size() oferece um resultado idêntico.9 Para a rede em análise, assume-se que contém

M links.

~~~Python

num_edges = G.number_of_edges()  
print(f"Número de Links (Arestas): {num_edges} links")
~~~

O número bruto de links, quando considerado em relação ao número de nós, oferece uma indicação imediata da esparsidade ou densidade da rede. Uma rede com muitos nós, mas relativamente poucas arestas, é considerada esparsa, o que pode sugerir conexões mais fracas ou menos numerosas, impactando o fluxo de informações. Em contraste, uma rede com um alto número de arestas em relação aos seus nós é densa, indicando uma forte interconectividade e, potencialmente, processos de difusão mais rápidos. Essa relação entre as contagens básicas de nós e arestas e uma propriedade de rede de nível superior, como a densidade ou o nível de conectividade, é fundamental para a compreensão inicial da estrutura.

### **C. Grau Médio (Average Degree)**

O grau médio, ⟨k⟩, é a média do número de conexões por nó na rede, oferecendo um resumo conciso do nível de conectividade geral da rede.

Para redes não direcionadas, o grau médio é calculado como

2M/N, uma vez que cada aresta contribui para o grau de dois nós, ou simplesmente como a soma de todos os graus dividida pelo número de nós. Em redes direcionadas, o grau médio de entrada (in-degree), o grau médio de saída (out-degree) e o grau total médio são matematicamente equivalentes a M/N. Contudo, para uma compreensão mais aprofundada de redes direcionadas, é frequentemente mais relevante teoricamente examinar as distribuições de in-degree e out-degree separadamente.

É importante notar que o NetworkX não possui uma função direta average\_degree() que retorne um único valor flutuante representando o grau médio de toda a rede. A função nx.average\_degree\_connectivity() calcula uma métrica diferente e mais complexa: o grau médio do vizinho mais próximo para nós de um grau

k específico. Esta é uma medida de assortatividade (correlação de graus) e não deve ser confundida com o grau médio simples. O grau médio deve ser calculado manualmente, somando todos os graus dos nós e dividindo pelo número de nós, ou utilizando as fórmulas 2M/N (para grafos não direcionados) ou M/N (para grafos direcionados).

~~~Python

# Cálculo do grau médio para um grafo não direcionado  
# Para grafos direcionados, o cálculo seria G.number_of_edges() / G.number_of_nodes()  
if G.is_directed():  
    avg_degree = G.number_of_edges() / G.number_of_nodes()  
    print(f"Grau Médio (Rede Direcionada): {avg_degree:.2f} passos")  
else:  
    avg_degree = (2 * G.number_of_edges()) / G.number_of_nodes()  
    print(f"Grau Médio (Rede Não Direcionada): {avg_degree:.2f} passos")

~~~

A distinção entre o grau médio e a conectividade média de grau (nx.average\_degree\_connectivity) é fundamental para evitar interpretações errôneas. Enquanto o grau médio fornece uma medida global da conectividade, a conectividade média de grau é uma métrica mais avançada que explora a correlação entre os graus dos nós conectados. Explicitar que

nx.average\_degree\_connectivity não é o "Grau médio" solicitado, mas sim uma medida de assortatividade, demonstra uma compreensão aprofundada das nuances da biblioteca e orienta a metodologia para resultados precisos.


### **D. Distribuição de Graus (Degree Distribution)**

A distribuição de graus, P(k), quantifica a probabilidade de um nó selecionado aleatoriamente na rede ter exatamente k conexões. Esta é uma descrição poderosa da heterogeneidade da rede, revelando padrões como a presença de nós "hub" altamente conectados ou uma distribuição mais uniforme de conexões. Para redes direcionadas, é essencial analisar separadamente a distribuição de in-degree (

Pin​(k)), que representa as conexões de entrada, e a distribuição de out-degree (Pout​(k)), que representa as conexões de saída. Essas distribuições frequentemente revelam papéis funcionais distintos para os nós, como receptores de informação versus emissores de informação.

Metodologia de Cálculo e Visualização:  
O processo de cálculo envolve primeiro a obtenção do grau (ou in-degree/out-degree para grafos direcionados) de cada nó na rede. Em seguida, a frequência de cada valor de grau único é contada para construir a distribuição.  
As técnicas de visualização são cruciais para a compreensão e comunicação dos resultados da análise da distribuição de graus.

* **Histograma:** Um histograma dos graus fornece uma representação visual da frequência (ou probabilidade) de nós com um determinado grau. Isso oferece uma percepção imediata da forma da distribuição e dos valores de grau mais comuns.
* **Gráfico Log-Log:** Plotar a distribuição de graus em uma escala log-log é essencial para identificar o comportamento de lei de potência (scale-free). Nesses tipos de distribuição, os pontos de dados tendem a se aproximar de uma linha reta em um gráfico log-log, indicando a presença de poucos nós "hub" altamente conectados e muitos nós com poucas conexões. Isso contrasta fortemente com redes aleatórias, que tipicamente exibem uma distribuição de Poisson (uma curva em forma de sino).

~~~Python

degree_sequence = sorted([d for n, d in G.degree()], reverse=True) # Para grafo não direcionado  
# Para grafo direcionado, usar:  
# degree_sequence = sorted([d for n, d in G.out_degree()], reverse=True) # Exemplo para out-degree

degree_counts = collections.Counter(degree_sequence)  
deg, cnt = zip(*degree_counts.items())

# Filtrar contagens zero para o gráfico log-log (logaritmo de zero é indefinido)  
positive_cnt_indices = np.array(cnt) > 0  
logx = np.log10(np.array(deg)[positive_cnt_indices])  
logy = np.log10(np.array(cnt)[positive_cnt_indices])

# Histogram Plot  
plt.figure(figsize=(10, 6))  
plt.bar(deg, cnt, width=0.8, color='b')  
plt.title("Histograma da Distribuição de Graus")  
plt.xlabel("Grau (k)")  
plt.ylabel("Número de Nós")  
plt.show()

# Log-Log Plot  
plt.figure(figsize=(10, 6))  
plt.plot(logx, logy, 'o', color='r', alpha=0.7)  
plt.title("Distribuição de Graus (Escala Log-Log)")  
plt.xlabel("log10(Grau)")  
plt.ylabel("log10(Número de Nós)")  
plt.grid(True, which="both", ls="-", alpha=0.2)  
plt.show()
~~~

Para uma análise mais rigorosa, a distribuição de graus empírica pode ser ajustada estatisticamente a modelos teóricos (e.g., Poisson, Lei de Potência, Exponencial) utilizando métodos como a estimativa de máxima verossimilhança ou testes de hipótese como o teste de Kolmogorov-Smirnov.

**Tabela 2: Distribuição de Frequência de Graus**

| Grau (k) | Número de Nós com Grau k (Frequência Absoluta) | Fração de Nós com Grau k (Frequência Relativa, P(k)) |
| :---- | :---- | :---- |
| k1​ | C1​ | P(k1​) |
| k2​ | C2​ | P(k2​) |
| ... | ... | ... |
| kn​ | Cn​ | P(kn​) |

A Tabela 2 fornece os dados numéricos brutos que fundamentam as representações gráficas da distribuição de graus. Ela permite uma inspeção precisa da frequência de cada valor de grau específico, o que é crucial para verificar os padrões observados nos gráficos, como as contagens exatas de nós "hub" ou a frequência de nós de baixo grau.

Figura 1: Histograma da Distribuição de Graus  
Esta visualização oferece uma compreensão imediata e intuitiva da forma geral da distribuição de graus, destacando os valores de grau mais comuns e a dispersão da conectividade entre os nós. É uma ferramenta fundamental para a exploração inicial da heterogeneidade da rede.  
Figura 2: Distribuição de Graus em Escala Log-Log  
Este gráfico de dispersão é indispensável para identificar se a rede empírica exibe uma distribuição de graus de lei de potência (scale-free). Se os pontos de dados se aproximam de uma linha reta nesta escala, isso sugere fortemente a presença de nós "hub" e tem implicações profundas para a robustez da rede e o fluxo de informações. Esta visualização é crítica para distinguir redes empíricas de modelos teóricos de grafos aleatórios.  
A forma identificada da distribuição de graus possui implicações profundas para a resiliência da rede e a propagação de informações. Redes de lei de potência (scale-free) são notavelmente robustas a falhas aleatórias de nós, pois a remoção de um nó aleatório é improvável de atingir um hub. No entanto, elas são altamente vulneráveis a ataques direcionados a seus nós hub críticos. Em contraste, redes aleatórias são mais suscetíveis à fragmentação por remoção aleatória de nós. Além disso, os hubs em redes de lei de potência atuam como emissores eficientes, facilitando a rápida disseminação de informações ou doenças. Essa relação direta de causa e efeito entre a propriedade estrutural da rede (distribuição de graus) e suas características funcionais (robustez, difusão) é um aspecto crucial da análise.

### **E. Média das Distâncias entre Pares (Average Shortest Path Length)**

A média das distâncias entre pares (ASPL), denotada como ⟨L⟩, é definida como o número médio de passos (arestas) ao longo dos caminhos mais curtos para todos os pares possíveis de nós na rede. Serve como uma medida crucial da eficiência da rede no transporte de informações ou massa. Um ASPL menor geralmente indica uma rede mais eficiente, interconectada e facilmente navegável, onde a informação pode viajar rapidamente entre quaisquer dois pontos.

O NetworkX fornece a função nx.average\_shortest\_path\_length(G, weight=None, method=None) para este cálculo. No entanto, é crucial observar que esta função é definida para grafos conectados. Ela levanta um

NetworkXError se o grafo não for conectado (para grafos não direcionados) ou não for fortemente conectado (para grafos direcionados).

**Manuseio de Grafos Desconectados:** Se a rede empírica for desconectada, o ASPL para o grafo inteiro é indefinido. Nesses casos, a prática padrão é calcular o ASPL para cada componente conectado. O relatório deve primeiro identificar esses componentes (e.g., usando nx.connected\_components(G) para grafos não direcionados ou nx.strongly\_connected\_components(G) para grafos direcionados) e, em seguida, aplicar a função a cada componente com mais de um nó.

~~~Python

if nx.is_connected(G):  
    avg_path_length = nx.average_shortest_path_length(G)  
    print(f"Média das Distâncias entre Pares: {avg_path_length:.2f} passos")  
else:  
    print("A rede é desconectada. Calculando a Média das Distâncias entre Pares para cada componente conectado.")  
    aspl_components =  
    for i, component in enumerate(nx.connected_components(G)):  
        subgraph = G.subgraph(component).copy() # Usar.copy() para evitar modificar o grafo original  
        if len(subgraph) > 1: # ASPL é indefinido para componentes de nó único  
            component_aspl = nx.average_shortest_path_length(subgraph)  
            aspl_components.append(component_aspl)  
            print(f"  Componente {i+1} (N={len(subgraph)}): {component_aspl:.2f} passos")  
    if aspl_components:  
        print(f"Média das Distâncias entre Pares (componentes): {np.mean(aspl_components):.2f} passos")  
    else:  
        print("Nenhum componente com mais de um nó para calcular a ASPL.")
~~~
Assumindo que a rede é conectada ou que o ASPL é calculado para seus componentes, a média das distâncias entre pares é X passos. Um ASPL curto, especialmente quando combinado com um coeficiente de agrupamento relativamente alto (uma medida de interconectividade local, embora não explicitamente solicitada, é uma métrica complementar comum), é a característica definidora das redes de "mundo pequeno". Essa propriedade, observada em muitas redes do mundo real (e.g., redes sociais, redes biológicas, a Internet), implica alta navegabilidade e processos de difusão eficientes, onde a informação ou influência pode se espalhar rapidamente por todo o sistema, apesar de seu grande tamanho.

### **F. Diâmetro da Rede (Diameter)**

O diâmetro de uma rede é definido como o caminho mais curto mais longo entre quaisquer dois nós na rede. Ele representa a separação máxima ou a "distância" que a informação ou influência deve percorrer dentro da rede. É uma métrica crítica para entender a compactação geral da rede, sua eficiência e potenciais gargalos. Um diâmetro menor geralmente indica uma rede mais interconectada e eficiente.

O NetworkX fornece a função nx.diameter(G, e=None, usebounds=False, weight=None). Assim como o ASPL,

nx.diameter() é definida para grafos conectados e levanta um NetworkXError se o grafo não for conectado (para grafos não direcionados) ou não for fortemente conectado (para grafos direcionados).

**Manuseio de Grafos Desconectados:** Para grafos desconectados, o diâmetro é tecnicamente infinito. Na análise de redes prática, o diâmetro é tipicamente calculado para o maior componente conectado, pois ele representa o "alcance" máximo dentro da parte mais extensa da rede. O NetworkX também oferece nx.algorithms.approximation.distance\_measures.diameter(), que calcula um limite inferior para o diâmetro e pode ser usado para grafos muito grandes onde o cálculo exato é inviável, mas também levanta um erro para grafos desconectados.

~~~Python

if nx.is_connected(G):  
    diameter = nx.diameter(G)  
    print(f"Diâmetro da Rede: {diameter} passos")  
else:  
    print("A rede é desconectada. O diâmetro é indefinido para a rede completa. Calculando para o maior componente conectado.")  
    largest_cc = max(nx.connected_components(G), key=len)  
    subgraph_lcc = G.subgraph(largest_cc).copy()  
    if len(subgraph_lcc) > 1:  
        diameter_lcc = nx.diameter(subgraph_lcc)  
        print(f"  Diâmetro do Maior Componente Conectado (N={len(subgraph_lcc)}): {diameter_lcc} passos")  
    else:  
        print("O maior componente conectado possui apenas um nó; diâmetro não aplicável.")
~~~


O diâmetro da rede é D passos. Um diâmetro grande, especialmente em relação ao tamanho da rede, pode indicar uma rede menos eficiente onde a informação ou os recursos podem levar um número significativo de passos para atravessar de um extremo ao outro. Isso destaca potenciais gargalos estruturais ou áreas onde o fluxo de comunicação pode ser lento. Por outro lado, um diâmetro pequeno, particularmente em redes grandes, reforça a propriedade de "mundo pequeno" (discutida com o ASPL) e sugere alta navegabilidade, onde quaisquer dois nós podem ser alcançados rapidamente. Essa conexão entre o diâmetro numérico e as implicações práticas para o design da rede, os protocolos de comunicação e o desempenho geral é um aspecto crucial.

