import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1
    return count

def get_neighbours(state):
    neighbours = []
    i = state.index(0)
    row = i // 3
    col = i % 3

    if row > 0:
        new = list(state)
        new[i], new[i-3] = new[i-3], new[i]
        neighbours.append(tuple(new))

    if row < 2:
        new = list(state)
        new[i], new[i+3] = new[i+3], new[i]
        neighbours.append(tuple(new))

    if col > 0:
        new = list(state)
        new[i], new[i-1] = new[i-1], new[i]
        neighbours.append(tuple(new))

    if col < 2:
        new = list(state)
        new[i], new[i+1] = new[i+1], new[i]
        neighbours.append(tuple(new))

    return neighbours

def a_star(start):
    h = heuristic(start)
    heap = [(h, 0, start, [start])]
    visited = set()

    while heap:
        f, g, state, path = heapq.heappop(heap)

        if state == GOAL:
            return path, g

        if state in visited:
            continue
        visited.add(state)

        for neighbour in get_neighbours(state):
            if neighbour not in visited:
                new_g = g + 1
                new_h = heuristic(neighbour)
                new_f = new_g + new_h
                heapq.heappush(heap, (new_f, new_g, neighbour, path + [neighbour]))

    return None, -1

def print_board(state, step=0):
    print(f"Step {step}:")
    for i in range(0, 9, 3):
        row = [str(t) if t != 0 else '_' for t in state[i:i+3]]
        print("  " + " | ".join(row))
        if i < 6:
            print("  ---------")
    print()

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

print("=" * 35)
print("   A* Algorithm - 8 Puzzle Game")
print("=" * 35)

print("\nStart State:")
print_board(start)

print("Goal State:")
print_board(GOAL)

path, moves = a_star(start)

if path:
    print(f"Solution found in {moves} moves!\n")
    print("Step-by-step solution:")
    for step, state in enumerate(path):
        print_board(state, step)
else:
    print("No solution exists!")