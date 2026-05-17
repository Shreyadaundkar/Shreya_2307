
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
prev = {n: None for n in graph}     
dist['A'] = 0
heap = [(0, 'A')]

while heap:
    d, u = heapq.heappop(heap)
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            prev[v] = u              # came from u
            heapq.heappush(heap, (dist[v], v))


print("Dijkstra's Shortest Paths from A:")
for node in graph:
    path, cur = [], node
    while cur:                       
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    print(f"  A -> {node} = {dist[node]}  | path: {' -> '.join(path)}")
