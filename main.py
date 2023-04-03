# Python 3 program for the
# haversine formula
import math
import heapq
import networkx as nx
import matplotlib.pyplot as plt
# Python 3 program for the
# haversine formula

def angle_between_3_points(x1, y1, x2, y2, x3, y3): # > 0 cua trai, < 0 cua phai
    # Tính vector AB và AC
    vector_ab = [x2 - x1, y2 - y1]
    vector_ac = [x3 - x1, y3 - y1]

    # Tính độ dài của vector AB và AC
    mag_ab = math.sqrt(vector_ab[0]**2 + vector_ab[1]**2)
    mag_ac = math.sqrt(vector_ac[0]**2 + vector_ac[1]**2)

    # Tính cos của góc giữa hai vector
    dot_product = vector_ab[0]*vector_ac[0] + vector_ab[1]*vector_ac[1]
    cos_angle = dot_product / (mag_ab * mag_ac)

    # Tính góc giữa hai vector và đổi sang đơn vị độ
    theta = math.degrees(math.acos(cos_angle))

    # Tính hướng của góc
    if vector_ab[0]*vector_ac[1] > vector_ab[1]*vector_ac[0]:
        theta = -theta

    return theta

#endDef

c = 0
def haversine(lat1, lon1, lat2, lon2):
     
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    global lat1_r
    lat1_r = (lat1) * math.pi / 180.0
    lat2_r = (lat2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1_r) * math.cos(lat2_r));
    rad = 6371
    global c
    c = 2 * math.asin(math.sqrt(a))
    return rad * c
 
# Tạo đồ thị
G = nx.DiGraph()

# Thêm các đỉnh với tọa độ GPS
G.add_node("A", pos=(10.879085008985427, 106.80808617842543)) # bat dau
G.add_node("B", pos=(10.878878272114965, 106.80795221093172)) # Ngã tu A17 A8
G.add_node("C", pos=(10.878325311804613, 106.80759865453054)) # ngã tu A8 A7
G.add_node("D", pos=(10.878049657760597, 106.80740899371546)) # gan A7 Tram Y Te
G.add_node("E", pos=(10.87906100884945, 106.8076574493876)) # Veo vao A8
G.add_node("F", pos=(10.878686641725384, 106.80825298433915)) # veo qua nha xe
G.add_node("G", pos=(10.879261091252419, 106.80732052414642)) # Nga 3 A15 A9
G.add_node("H", pos=(10.878972912720549, 106.80712914202557)) # Giua A9
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True)

# Thêm các cạnh và trọng số
G.add_edge("A", "B", weight=haversine(pos['A'][0],pos['A'][1],pos['B'][0],pos['B'][1]))
G.add_edge("A", "C", weight=haversine(pos['A'][0],pos['C'][1],pos['B'][0],pos['C'][1]))
G.add_edge("A", "D", weight=haversine(pos['A'][0],pos['A'][1],pos['D'][0],pos['D'][1]))
G.add_edge("B", "E", weight=haversine(pos['B'][0],pos['B'][1],pos['E'][0],pos['E'][1]))
G.add_edge("B", "F", weight=haversine(pos['B'][0],pos['B'][1],pos['F'][0],pos['F'][1]))
G.add_edge("B", "G", weight=haversine(pos['B'][0],pos['B'][1],pos['G'][0],pos['G'][1]))
G.add_edge("G", "H", weight=haversine(pos['G'][0],pos['G'][1],pos['H'][0],pos['H'][1]))


labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#plt.show()

start_node = "A"
end_node = "H"
shortest_path = nx.dijkstra_path(G, start_node, end_node)

# In ra đường đi ngắn nhất
print("Đường đi ngắn nhất từ", start_node, "đến", end_node, "là:", shortest_path)
length = len(shortest_path)
print(length)
goc = angle_between_3_points(pos['A'][0], pos['E'][1], \
                             pos['B'][0], pos['B'][1], pos['C'][0], pos['C'][1])
#goc1 = angle_between(pos['A'],pos['B'],pos['F'])
print(goc)
#print(goc1)
i = 2

def kiemTra(lat, lon):
    global i
    khoangCach = haversine(lat,lon,pos[shortest_path[i-1]][0],pos[shortest_path[i - 1]][1]) * 1000
    print(khoangCach)
    if khoangCach < 3.5:
        if i < length:
            goc = angle_between_3_points(pos[shortest_path[i-2]][0], pos[shortest_path[i-2]][1], \
                                    pos[shortest_path[i-1]][0], pos[shortest_path[i-1]][1],\
                                          pos[shortest_path[i]][0], pos[shortest_path[i]][1])
            if goc > 0:
                print("cua trai")
                i = i + 1
            else:
                print("cua phai")
                i = i + 1
            #endIf
        else:
            print("dung xe")
        #endIf
    #endIf
#endFor

lat = 10.878880686283978
lon = 106.80794802825407
kiemTra(lat,lon)
print(i)
lat = 10.879267356000033
lon = 106.80731414474239
kiemTra(lat,lon)
print(i)
lat = 10.878966647966765
lon =  106.80712914202557
kiemTra(lat,lon)
print(i)
        






