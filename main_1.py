import math

coords = [
    (21.033333, 105.850000),
    (21.027763, 105.834160),
    (21.021602, 105.818118),
    (21.036386, 105.805088),
    (21.039070, 105.793105),
    (21.052364, 105.796972),
    (21.064834, 105.794064)
]

def taoDoThiCoHuong():
    f = open('doThiCoHuong.txt')
    soLuongDinh = int(f.readline().strip())
    cacDong = f.readlines()
    f.close()

    doThi = [[0 for _ in range(soLuongDinh)] for _ in range(soLuongDinh)]
    for dong in cacDong:
        dsGiaTri = dong.split()
        if len(dsGiaTri) != 3:
            continue
        else:
            dong = int(dsGiaTri[0])
            cot = int(dsGiaTri[1])
            khoangCach = int(dsGiaTri[2])
            doThi[dong][cot] = khoangCach
        #endIf
    #endFor
    return doThi
#endDef

dsDinhDiQua = 0

def layDuongDi(dsDinhtruoc, dinhDich):
    global dsDinhDiQua
    dsDinhDiQua = [dinhDich]
    dinh = dinhDich
    while True:
        dinh = dsDinhtruoc[dinh]
        if dinh == None:
            break
        else:
            dsDinhDiQua.insert(0,dinh)
        #endif
    #endWhile
    dsDinhDiQuaString = [str(x) for x in dsDinhDiQua]
    return ' -> '.join(dsDinhDiQuaString)
#endDef

def khoangCachMin(dsKhoangCach, dsDinhCayMin):
    nhoNhat = math.inf
    dinhNhoNhat = math.inf
    for dinh in range(len(dsKhoangCach)):
        if dsDinhCayMin[dinh] == False and dsKhoangCach[dinh] < nhoNhat:
            nhoNhat = dsKhoangCach[dinh]
            dinhNhoNhat = dinh
        #endIf
    #endFor
    return dinhNhoNhat
#endDef

def dijkstra(doThi, dinhNguon, dinhDich):
    soLuongDinh = len(doThi)
    #Khoang Cach toi cac dinh la vo cung
    dsKhoanhCach = [math.inf for _ in range(soLuongDinh)]
    #Khoang cach tu dinh nguon toi chinh no = 0
    dsKhoanhCach[dinhNguon] = 0
    dsDinhTruoc = [None for _ in range(soLuongDinh)]
    dsDinhCayMin = [False for _ in range(soLuongDinh)]

    for i in range(soLuongDinh):
        x = khoangCachMin(dsKhoanhCach, dsDinhCayMin)

        if x == math.inf:
            print(f'Khong co duong di dinh {dinhNguon} den dinh {dinhDich}')
            return
        #endIf

        dsDinhCayMin[x] = True
        if x == dinhDich:
            print(f'Tim thay duong di tu dinh {dinhNguon} den dinh {dinhDich}')
            duongDi = layDuongDi(dsDinhTruoc, dinhDich)
            thongBao = f'Tu dinh {dinhNguon} den dinh {dinhDich} : ' \
                + duongDi + ' : ' + str(dsKhoanhCach[dinhDich])
            print(thongBao)
            return
        else:
            for y in range(soLuongDinh):
                if dsDinhCayMin[y] == False \
                    and doThi[x][y] > 0 and dsKhoanhCach[y] > dsKhoanhCach[x] + doThi[x][y]:
                    dsKhoanhCach[y] = dsKhoanhCach[x] + doThi[x][y]
                    dsDinhTruoc[y] = x
                #endIf
            #endFor
        #endIf
    #endFor
#endDef

hello = [[0 for _ in range(len(coords))] for _ in range(len(coords))]
print(hello)


# doThi = taoDoThiCoHuong()
# print(doThi) 
# soLuongDinh = len(doThi)
# print('So Luong Dinh', soLuongDinh)
# dinhNguon = int(input('Nhap vao dinh nguon: '))
# dinhDich = int(input('Nhap vao dinh dich: '))
# if dinhNguon in range(soLuongDinh) and dinhDich in range(soLuongDinh):
#     dijkstra(doThi, dinhNguon, dinhDich)
# print(dsDinhDiQua)

#endIf

# # Driver code


# def create_graph(coords):
#     graph = {}
#     for i in range(len(coords)):
#         graph[i] = {}
#         for j in range(len(coords)):
#             if i != j:
#                 dist = haversine(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
#                 graph[i][j] = dist
#     return graph

# def dijkstra(start, end, graph):
#     # Khởi tạo khoảng cách ban đầu
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0

#     # Sử dụng heap để lưu trữ đỉnh và khoảng cách
#     pq = [(0, start)]
#     previous_vertices = {vertex: None for vertex in graph}

#     while len(pq) > 0:
#         current_distance, current_vertex = heapq.heappop(pq)

#         # Nếu đỉnh hiện tại là đỉnh đích, kết thúc thuật toán
#         if current_vertex == end:
#             path = []
#             while current_vertex is not None:
#                 path.append(current_vertex)
#                 current_vertex = previous_vertices[current_vertex]

#             return path[::-1]

#         # Nếu không, cập nhật khoảng cách đến các đỉnh kề
#         for neighbor, weight in graph[current_vertex].items():
#             distance = distances[current_vertex] + weight

#             # Nếu khoảng cách mới nhỏ hơn khoảng cách hiện tại, cập nhật
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 previous_vertices[neighbor] = current_vertex
#                 heapq.heappush(pq, (distance, neighbor))

#     return None

# # Ví dụ về cách sử dụng thuật toán
# coords = [
#     (21.033333, 105.850000),
#     (21.027763, 105.834160),
#     (21.021602, 105.818118),
#     (21.036386, 105.805088),
#     (21.039070, 105.793105),
#     (21.052364, 105.796972),
#     (21.064834, 105.794064)
# ]
# print(len(coords))
# graph = create_graph(coords)
# print(graph)
# start = 0
# end = 6

# path = dijkstra(start, end, graph)
# print(path)
# if path is not None:
#     for i in range(len(path) - 1):
#         print(f"Di chuyển từ {coords[path[i]]} đến {coords[path[i+1]]}")
# else:
#     print(f"Không tìm thấy đường đi từ {start} đến {end}")


