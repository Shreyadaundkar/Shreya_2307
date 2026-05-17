
import heapq

graph = {
    'A': [('B',2), ('D',6)],
    'B': [('A',2), ('C',3), ('E',5)],
    'C': [('B',3), ('E',7)],
    'D': [('A',6), ('E',9)],
    'E': [('B',5), ('C',7), ('D',9)]
}


visited = set()
heap = [(0, 'A', 'A')]   
mst, cost = [], 0

while heap:
    w, u, frm = heapq.heappop(heap)   
    if u in visited:                 
        continue
    visited.add(u)
    if u != frm:                      
        mst.append((frm, u, w))
        cost += w
    for v, wt in graph[u]:
        if v not in visited:
            heapq.heappush(heap, (wt, v, u))


print("Prim's MST:")
for u, v, w in mst:
    print(f"  {u} -- {v}  weight={w}")
print("Total Cost:", cost)
