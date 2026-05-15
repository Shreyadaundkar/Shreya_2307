graph={
    '1':['2','3'],
    '2':['3','4'],
    '4':['5'],
    '5':['6'],
    '6':['3','1'],
    '3':['7'],
    '7':['1']

}


def dfs(visited,graph,node):
    if node not in visited:
        visited.append(node)

        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
visited=[]
print("DFS traversal:")
dfs(visited,graph,'1')
print(visited)



graph={
    '1':['2','3'],
    '2':['3','4'],
    '4':['5'],
    '5':['6'],
    '6':['3','1'],
    '3':['7'],
    '7':['1']

}
  

visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS Traversal:")
bfs(visited,graph,'1')


