import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic cost from current node to goal node
        self.f = 0  # Total cost: f = g + h

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def astar(grid: list, start: tuple, goal: tuple) -> list:
    open_list = []
    closed_set = set()
    
    start_node = Node(None, start)
    goal_node = Node(None, goal)
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)
        
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        for neighbor in neighbors:
            neighbor_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])
            
            if (0 <= neighbor_position[0] < len(grid) and
                0 <= neighbor_position[1] < len(grid[0]) and
                grid[neighbor_position[0]][neighbor_position[1]] != 1 and
                neighbor_position not in closed_set):
                
                neighbor_node = Node(current_node, neighbor_position)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_position, goal_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h
                
                heapq.heappush(open_list, neighbor_node)
                closed_set.add(neighbor_position)

# Example usage; this will only execute if you run `main.py`:
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)

    path = astar(grid, start, goal)
    if path:
        path
    else:
        print("No path found")
