def astar(start_state, goal_state, get_neighbors, heuristic):
    start_node = (start_state, None, 0, heuristic(start_state, goal_state))
    open_list = [start_node]
    closed_set = set()
    while open_list:
        open_list.sort(key=lambda x: x[2] + x[3])
        current_state, parent, cost, _ = open_list.pop(0)
        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state, parent, _, _ = parent
            return list(reversed(path))
        closed_set.add(current_state)
        for neighbor_state, neighbor_cost in get_neighbors(current_state):
            if neighbor_state in closed_set:
                continue
            neighbor_node = (neighbor_state, (current_state, parent, cost, _), cost + neighbor_cost, heuristic(neighbor_state, goal_state))
            for i, open_node in enumerate(open_list):
                if open_node[0] == neighbor_state and open_node[2] + open_node[3] < neighbor_node[2] + neighbor_node[3]:
                    break
            else:
                open_list.append(neighbor_node)
    return None
def get_neighbors(state):
    neighbors = []
    return neighbors
def heuristic(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)
start_state = (0, 0)
goal_state = (3, 4)
path = astar(start_state, goal_state, get_neighbors, heuristic)
print("Optimal Path:", path)
