
import heapq


graph = {
    'A': [('B',4), ('C',2)],
    'B': [('D',10)],
    'C': [('E',3)],
    'D': [('F',11)],
    'E': [('D',4), ('F',7)],
    'F': []
}


dist = {n: float('inf') for n in graph} 
dist['A'] = 0                             
heap = [(0, 'A')]                        

while heap:
    d, u = heapq.heappop(heap)            
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:        
            dist[v] = dist[u] + w
            heapq.heappush(heap, (dist[v], v))


print("Shortest Distances from A:")
for node, d in dist.items():
    print(f"  A -> {node} = {d}")
