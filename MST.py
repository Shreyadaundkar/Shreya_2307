
parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])   
    return parent[x]

def union(x, y):
    if find(x) == find(y):           
        return False
    parent[find(y)] = find(x)         
    return True

edges = [(2,'A','B'),(3,'B','C'),(5,'B','E'),
         (6,'A','D'),(7,'C','E'),(8,'B','D'),(9,'D','E')]

nodes = ['A','B','C','D','E']
for n in nodes:
    parent[n] = n                    


edges.sort()
mst, cost = [], 0

for w, u, v in edges:
    if union(u, v):                  
        mst.append((u, v, w))
        cost += w

# --- Output ---
print("MST Edges:")
for u, v, w in mst:
    print(f"  {u} -- {v}  weight={w}")
print("Total Cost:", cost)
