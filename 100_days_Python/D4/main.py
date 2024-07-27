import heapq

class AStar:
    def __init__(self, start, goal, grid):
        self.start = start
        self.goal = goal
        self.grid = grid
        self.open_list = []
        heapq.heappush(self.open_list, (0, self.start))
        self.came_from = {}
        self.g_score = {start: 0}
        self.f_score = {start: self.heuristic(start, goal)}
    
    def heuristic(self, a, b):
        # Using Manhattan distance as the heuristic function
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def neighbors(self, node):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            if 0 <= neighbor[0] < len(self.grid) and 0 <= neighbor[1] < len(self.grid[0]) and self.grid[neighbor[0]][neighbor[1]] == 0:
                result.append(neighbor)
        return result
    
    def search(self):
        while self.open_list:
            _, current = heapq.heappop(self.open_list)
            if current == self.goal:
                return self.reconstruct_path(current)
            for neighbor in self.neighbors(current):
                tentative_g_score = self.g_score[current] + 1  # Assume each move has a cost of 1
                if neighbor not in self.g_score or tentative_g_score < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g_score
                    self.f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.goal)
                    heapq.heappush(self.open_list, (self.f_score[neighbor], neighbor))
        return None
    
    def reconstruct_path(self, current):
        total_path = [current]
        while current in self.came_from:
            current = self.came_from[current]
            total_path.append(current)
        return total_path[::-1]

# Example grid where 0 represents walkable path and 1 represents obstacle
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

astar = AStar(start, goal, grid)
path = astar.search()

print("Shortest path from start to goal:", path)
