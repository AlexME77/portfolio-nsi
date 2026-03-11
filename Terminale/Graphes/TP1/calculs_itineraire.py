from math import *
import osmnx as ox
import networkx as nx
import folium
from IPython.display import IFrame
from geopy.geocoders import Nominatim
ox.config(log_console=True, log_file=True, use_cache=True)
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

#fonction déterminant les coordonnées GPS à partir d'une adresse postale
def coord_GPS_addresse(adresse, ville):
    geo = Nominatim()
    coord = geo.geocode(adresse + ' ' + ville, timeout = 10)
    coord_GPS=(coord.latitude,coord.longitude)
    return(coord_GPS)

#fonction calcul de la distance entre deux points GPS en mètres
def distance_2pGPS(coord1,coord2):
    la1=radians(coord1[0])
    la2=radians(coord2[0])
    lon1=radians(coord1[1])
    lon2=radians(coord2[1])
    dis=6371009*acos((sin(la1)*sin(la2)+cos(la1)*cos(la2)*cos(lon1-lon2)))
    return dis

#fonction de calculs d'orientation d'une droite passant par 2 points GPS par rapport à la direction Nord
def orientation(coord1,coord2):
    la1=radians(coord1[0])
    la2=radians(coord2[0])
    lon1=radians(coord1[1])
    lon2=radians(coord2[1])
    longDelta = lon2-lon1
    y= sin(longDelta)*cos(la1)
    x=cos(la1)*sin(la2)-sin(la1)*cos(la2)*cos(longDelta)
    angle = atan2(y,x)*360/(2*pi)
    while angle < 0:
        angle += 360
    direction=360-(float(angle) % 360)
    return direction

# fonction calcul du temps de parcours du chemin le plus court en tenant compte des vitesses maximums renseignées sur openstreetmap
def calcul_temps_parcours(G,route):
    t=0
    distance=0
    d=0
    edges_proj = ox.graph_to_gdfs(G, nodes=False, edges=True)
    for i in range (0 ,len(route)-1):
        d=distance_2pGPS((G.node[route[i]]['y'],G.node[route[i]]['x']),(G.node[route[i+1]]['y'],G.node[route[i+1]]['x']))
        for j in range(0,len(edges_proj.osmid)):
            if (edges_proj.u[j]==route[i]) and (edges_proj.v[j]==route[i+1]):
                v= float(edges_proj.maxspeed[j])
                if isnan(v) :
                    road=edges_proj.highway[j]
                    if road=='unclassified' or road[0]=='unclassified' :
                        v=30
                        break;
                    if road== 'residential'  or road[1]=='residential':
                        v=30
                        break;
                    if road== 'tertiary'  or road[1]=='tertiary':
                        v=80
                        break;
        t+= (d*3.6)/v
        distance = distance + d
    return(t)


# génération d'une carte interactive itineraire.html avec tous les détails
def graphique_html(G,route):
    graph_map = ox.plot_graph_folium(G, popup_attribute='name',  edge_width=2)
    route_graph_map= ox.plot_route_folium(G, route, route_map=graph_map, popup_attribute='length')
    folium.Marker(location=(G.node[route[0]]['y'],G.node[route[0]]['x']), icon=folium.Icon(color='red')).add_to(route_graph_map)
    folium.Marker(location=(G.node[route[len(route)-1]]['y'],G.node[route[len(route)-1]]['x']), icon=folium.Icon(color='blue')).add_to(route_graph_map)
    filepath = 'itinéraire.html'
    route_graph_map.save(filepath)
    IFrame(filepath, width=600, height=500)

#génération du graphe de la zone géographique incluant l'itinéraire en fonction du type de moyen de locomotion
def graphe(adresse_depart,Ville_D,adresse_arrivee,Ville_A,type_graph):
    origine_GPS=coord_GPS_addresse(adresse_depart,Ville_D)
    destination_GPS=coord_GPS_addresse(adresse_arrivee,Ville_A)
    point = ((origine_GPS[0]+destination_GPS[0])/2,(origine_GPS[1]+destination_GPS[1])/2)
    dist=distance_2pGPS(origine_GPS,destination_GPS)/1.5
    G = ox.graph_from_point(point, distance=dist, network_type=type_graph)
    origine=ox.get_nearest_node(G, origine_GPS)
    destination=ox.get_nearest_node(G, destination_GPS)
    route = nx.shortest_path(G, origine, destination)
    ox.plot_graph_route(G,route,fig_height=10, fig_width=10, show=True, use_geom=True, close=False, route_color='green' ,orig_dest_node_size=100)
    return G, route


# Algorithme de calcul de distance à rechercher par les élèves en TP
def calcul_distance(G, route):
    distance_totale=0.0
    for i in range(len(route)-1):
        sommet_courant = route[i]
        sommet_suivant = route[i+1]
        coord1 = (G.node[sommet_courant]['y'], G.node[sommet_courant]['x'])
        coord2 = (G.node[sommet_suivant]['y'], G.node[sommet_suivant]['x'])
        distance_segment = distance_2pGPS(coord1, coord2)
        distance_totale+=distance_segment
    return distance_totale

def calcul_distance_arrete(G, route):
    distance_totale = 0.0
    for i in range(len(route)-1):
        sommet_u = route[i]
        sommet_v = route[i+1]
        distance_segment = G[sommet_u][sommet_v][0]['length']
        distance_totale += distance_segment
    return distance_totale

def calcul_temps_trajet(distance, vitesse):
    vitesse_ms = vitesse/3.6
    return distance/vitesse_ms


# Programme principal
if __name__=='__main__':
    #coord_GPS_maison=coord_GPS_addresse("14 rue de la biche","Chelles")
    #coord_GPS_lycee=coord_GPS_addresse("32 avenue de l'europe","Chelles")
    #print("Coordonnées GPS maison : ", coord_GPS_maison)
    #print("Coordonnées GPS lycée : ", coord_GPS_lycee)
    #graphe("14 rue de la biche","Chelles","32 avenue de l'europe","Chelles","drive_service")
    #graphe("14 rue de la biche","Chelles","32 avenue de l'europe","Chelles","walk")
    G_drive, route_drive = graphe("14 rue de la biche","Chelles","32 avenue de l'europe","Chelles","drive")
    #print("Route voiture : ", route_drive)
    #graphique_html(G_drive, route_drive)
    #print("Orientation par rapport au Nord entre mon domicile et le lycée : ", orientation(coord_GPS_maison, coord_GPS_lycee))
    distance = calcul_distance(G_drive, route_drive)
    #print(distance)
    #distance_arrete = calcul_distance_arrete(G_drive.adj, route_drive)
    #print(distance_arrete)
    #print(calcul_temps_trajet(distance, 50), 'secondes')
    print(calcul_temps_trajet(distance, 20))