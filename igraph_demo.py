import igraph as ig
import networkx as nx
import math

def major_centralities(eb, number_of_centralities):
    major = [[-1, -math.inf] for i in range(number_of_centralities)]

    for i in range(len(eb)):
        if eb[i] > major[number_of_centralities-1][1]:
            major[number_of_centralities-1][1] = eb[i]
            major[number_of_centralities-1][0] = i
            pos = number_of_centralities-2
            while pos >= 0 and eb[i] > major[pos][1]:
                major[pos+1][1] = major[pos][1]
                major[pos+1][0] = major[pos][0]
                major[pos][1] = eb[i]
                major[pos][0] = i
                pos-=1
    return major

def cliques_sizes(cliques):
    sizes = []
    for i in cliques:
        sizes.append(len(i))
    return sizes

karate = nx.karate_club_graph()
kite = nx.krackhardt_kite_graph()

graph = ig.Graph.from_networkx(kite)
ig.plot(graph, layout='auto', vertex_label=graph.vs['_nx_name'])

#atributos
layout = graph.layout()
coords = layout.coords
dim = layout.dim

#medidas de centalidade
closeness = graph.closeness()
betweenness = graph.betweenness()
eigenvector = graph.eigenvector_centrality()

#centralidade de intermediação de arestas
eb = graph.edge_betweenness()
majors = major_centralities(eb, 3)

#cliques
cliques = graph.cliques()
sizes = cliques_sizes(cliques)

#core
cores = graph.coreness()

#densidade
density = graph.density()
