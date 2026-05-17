graph={
    '1':['2','3'],
    '2':['3','4'],
    '4':['5'],
    '5':['6'],
    '6':['3','1'],
    '3':['7'],
    '7':['1']

}


def breadthFirstSearch(visited, graph, node):
    visited.append(node)       
    queue.append(node)         

    while queue:               
        m = queue.pop(0)       
        print(m, end=" ")     

        for neighbour in graph[m]:           
            if neighbour not in visited:    
                visited.append(neighbour)    
                queue.append(neighbour)      


def depthFirstSearch(visited, graph, node):
    if node not in visited:              
        print(node, end=" ")             
        visited.add(node)               

        for neighbour in graph[node]:    
            depthFirstSearch(visited, graph, neighbour)  


while True:
    print("\n=============================")
    print("       GRAPH MENU")
    print("=============================")
    print("  1. Breadth First Search (BFS)")
    print("  2. Depth First Search (DFS)")
    print("  3. Display Graph")
    print("  4. Exit")
    print("=============================")

    choice = input("Enter your choice: ")   

    if choice == '1':
        
        visited = []   
        queue = []      
        print("\nBreadth-First Search:")
        breadthFirstSearch(visited, graph, '1')  
        print()

    elif choice == '2':
       
        visited = set()  
        print("\nDepth-First Search:")
        depthFirstSearch(visited, graph, '1')    
        print()

    elif choice == '3':
        # Show the graph
        print("\nGraph (Adjacency List):")
        for node in graph:
            print(f"  {node} --> {graph[node]}")

    elif choice == '4':
        print("Exiting... Goodbye!")
        break

        print("Invalid choice! Enter 1 to 4.")