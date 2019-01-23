
from Graph import Graph, Vertex
import sys
import itertools
import heapq
            

def shortest(u,v, path): #for printing path
    ''' make shortest path from v.previous'''
    if v.previous!=u and v.previous:
        path.append(v.previous.get_id())
      
        shortest(u,v.previous, path)
    return


def dijkstra(aGraph, start, target):
   # print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    for v in aGraph:
        v.set_distance(sys.maxsize)
        v.set_previous(None)
        v.visited = False
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
               
        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    return target.get_distance()

def ways_combinations(start, target, stops): 
    ways = []
    ways_temp = list(itertools.permutations(stops, len(stops)))
    for way in ways_temp:
        way=list(way)
        ways.append([start]+way+[target])
    return ways

def compute(g,ways):
    short = sys.maxsize
    ind = -1
    path_list=[]
    answer = []
    for way in range(len(ways)):
        path = 0
        temp_path=[ways[0][0]]
        for i in range(len(ways[way])-1):
            path += dijkstra(g, g.get_vertex(ways[way][i]), g.get_vertex(ways[way][i+1]))
            
            start = g.get_vertex(ways[way][i])
            target = g.get_vertex(ways[way][i+1])
      
            p = [ways[way][i+1]]
            
            shortest(start,target, p)
            p = p[::-1]
            temp_path = temp_path + p
        heapq.heappush(path_list,(temp_path, path))
        if short > path:
            short = path
            ind = way
  
    
    while len(path_list)>0 and path_list[0][1]==short:
    
        answer.append(heapq.heappop(path_list))

    return answer



def proceed_input():
    edges = []
    pathes = [] #[start, target, [stops]]
    edges_num = int(raw_input())
    for edge in range(edges_num):
        tmp = raw_input().split() #[vert, vert, weight]
        edges.append(tmp)
    pathes_num = int(raw_input())
    for path in range(pathes_num):
        path = []
        tmp = raw_input().split() #[stops_num, stop..]
        stops_num = int(tmp[0])
        path.append(tmp[1])
        path.append(tmp[2])
        tmp_stop = []
        for stop in range(stops_num):
            tmp_stop.append(raw_input())
        path.append(tmp_stop)
        pathes.append(path)
    return edges, pathes

edges, pathes = proceed_input()
print(edges,pathes)
graph = Graph()
for edge in edges:
    graph.add_edge(edge[0], edge[1], int(edge[2]))
for path in range(len(pathes)):
    print "case " + str(path+1)
    ways = ways_combinations(pathes[path][0], pathes[path][1], pathes[path][2])
    answers = compute(graph, ways)
    if answers==[]:
        print 'No path'
    else:
        print(answers[0][1])
        for i in range(len(answers)):
            print(answers[i][0])
            

        ##tests
            
''' 
g = Graph()
g.add_edge("Berlin", "Amsterdam", 4)
g.add_edge("Berlin", "Frankfurt", 1)
g.add_edge("Berlin", "Praha", 2)
g.add_edge("Berlin", "Zurich", 9)
g.add_edge("Amsterdam", "Frankfurt", 2)
g.add_edge("Amsterdam", "London", 4)
g.add_edge("Amsterdam", "Paris", 5)
g.add_edge("Frankfurt", "Zurich", 7)
g.add_edge("Praha", "Paris", 11)
g.add_edge("Praha", "Wien", 6)
g.add_edge("London", "Paris", 3)
g.add_edge("London", "Rome", 6)
g.add_edge("Paris", "Zurich", 1)
g.add_edge("Zurich", "Wien", 5)
g.add_edge("Zurich", "Rome", 4)
g.add_edge("Wien", "Rome", 6)



print("###############################")
ways = ways_combinations("Wien", "London", ["Berlin", "Zurich"])
answer = compute(g, ways)
print answer
print("###############################")
ways = ways_combinations("Berlin", "Rome", [])
answer = compute(g, ways)
print answer
'''