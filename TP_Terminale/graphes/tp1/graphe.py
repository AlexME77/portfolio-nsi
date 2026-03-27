from PileFile import PileFile
import networkx as nx
import matplotlib.pyplot as plt

class graphe:

    def __init__(self, graphe):
        self.__graphe = graphe

    def dijkstra(self, mat_adj, sommet_depart, sommet_arrivee):
        observe=PileFile()
        visite=[]
        chemin=[]
        dejavu=[]
        cycle=False
        observe.enfiler(sommet_depart)
        distance={sommet_depart:0}
        while not observe.estVide():
            sommet=observe.defiler()
            if sommet in visite:
                cycle=True
            for voisin in mat_adj[sommet]:
                observe.enfiler(voisin)
                nouvelle_distance=distance[sommet]+mat_adj[sommet][voisin]
                if voisin not in distance or nouvelle_distance < distance[voisin]:
                    distance[voisin]=nouvelle_distance
                    dejavu.append(voisin)
                    visite.append(sommet)
        chemin.append(sommet_arrivee)
        for i in range(len(dejavu)-1, -1, -1):
            if chemin[-1]==dejavu[i]:
                chemin.append(visite[i])
        if sommet_depart not in chemin:
                chemin.append(sommet_depart)
        chemin.reverse()
        return chemin, distance[sommet_arrivee], cycle

    def dessiner(self):
        G = nx.DiGraph()
        weighted_edges = []
        for node_p, nodes_s in self.__graphe.items():
            for node_s, weight in nodes_s.items():
                weighted_edges.append((node_p, node_s, weight))
        G.add_weighted_edges_from(weighted_edges)
        pos = nx.spring_layout(G, seed=2)
        nx.draw_networkx(G, pos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

if __name__ == "__main__":
    #Liste d'ajacence du graphe pour le test de l'algorithme
    adj = {'A':{'B':15,'C':4},'B':{'E':5},'C':{'E':11,'D':2},'D':{'E':3},'E':{}}
    adj_carte = {'Z':{'B':185, 'T':296},'B':{'T':245,'R':205},'T':{'R':200,'P':242},'R':{'C':179},'C':{'L':164,'P':332},'P':{'V':203,'M':168},'L':{'V':102},'V':{'M':213}, 'M':{}}
    #Main
    mon_graphe = graphe(adj)
    mon_graphe_carte = graphe(adj_carte)
    print(str(mon_graphe.dijkstra(adj, 'A', 'E')))
    print(str(mon_graphe_carte.dijkstra(adj_carte, 'Z', 'L')))
    mon_graphe.dessiner()