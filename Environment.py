from collections import deque
import random
import math
class Env:
    def __init__(self, length, height, difficulty=1) -> None:
        '''
        0 -> food
        1 -> wall
        2 -> pacman
        3 -> ghost
        4 -> empty
        5 -> ghost
        '''
        self.length = length
        self.height = height
        self.board = [[0 for i in range(length)] for j in range(height)]
        self.food = [[1 for i in range(length)] for j in range(height)]
        self.difficulty = difficulty
        if difficulty == 0:
            pass
        else:
            wall = [1 for i in range(difficulty * 9)]
        for i in range(difficulty * 9):
            x, y = random.randint(1, height - 1), random.randint(1, length - 1)
            self.board[x][y] = wall[i]

    def insert_agent(self, agent):
        if agent.type == 2:
            self.board[agent.pos[0]][agent.pos[1]] = 2
        else:
            if(self.board[agent.pos[0]][agent.pos[1]]) == 4:
                self.board[agent.pos[0]][agent.pos[1]] = 3

            elif(self.board[agent.pos[0]][agent.pos[1]] == 0):
                self.board[agent.pos[0]][agent.pos[1]] = 5
    def remove_agent(self, agent):
        if agent.type==3:
            if self.board[agent.pos[0]][agent.pos[1]] == 5:
                self.board[agent.pos[0]][agent.pos[1]] = 0
            else:
                self.board[agent.pos[0]][agent.pos[1]] = 4
        else:
            self.board[agent.pos[0]][agent.pos[1]] = 4
            
    def step(self, agent, action):
        self.remove_agent(agent)
        match action:
            case "right":
                agent.pos[1] = (agent.pos[1] + 1) % self.length
            case "left":
                agent.pos[1] = (agent.pos[1] - 1) % self.length
            case "down":
                agent.pos[0] = (agent.pos[0] + 1) % self.height
            case "up":
                agent.pos[0] = (agent.pos[0] - 1) % self.height
        self.insert_agent(agent)
        # self.food[agent.pos[0]][agent.pos[1]] = 0
        return self
    def is_wall(self,coord):
        if self.board[coord[0]][coord[1]] == 1:
            return True
        return False
    def is_food(self,coord):
        if self.board[coord[0]][coord[1]] == 0:
            return True
        return False
    def is_ghost(self,coord):
        if self.board[coord[0]][coord[1]] == 5:
            return True
        return False
    def get_neighbors(self, coord):
        neighbors = []
        for action in ["left","right","up","down"]:
            match action:
                case "right":
                    pos = [coord[0],((coord[1] + 1) % self.length)]
                    if not self.is_wall(pos) and not self.is_ghost(pos):
                        neighbors.append(('right',[coord[0],((coord[1] + 1) % self.length)]))
                case "left":
                    pos = [coord[0],((coord[1] - 1) % self.length)]
                    if not self.is_wall(pos) and not self.is_ghost(pos):
                        neighbors.append(('left',[coord[0],((coord[1] - 1) % self.length)]))
                case "down":
                    pos = [(coord[0] + 1) % self.height,coord[1]]
                    if not self.is_wall(pos) and not self.is_ghost(pos):
                        neighbors.append(('down',[(coord[0] + 1) % self.height,coord[1]]))
                case "up":
                    pos = [(coord[0] - 1) % self.height,coord[1]]
                    if not self.is_wall(pos) and not self.is_ghost(pos):
                        neighbors.append(('up',[(coord[0] - 1) % self.height,coord[1]]))
        return neighbors
    def find_nearest_food(self, position):
        min_distance = math.inf
        nearest_food = None

        for i in range(self.height):
            for j in range(self.length):
                if self.board[i][j] == 0:  # if the cell contains food
                    distance = abs(position[0] - i) + abs(position[1] - j)  # calculate Manhattan distance
                    if distance < min_distance:
                        min_distance = distance
                        nearest_food = (i, j)

        return nearest_food

    def find_shortest_path(self, start):
        start = tuple(start)

        # Directions for left, right, up, down
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        queue = deque([start])
        visited = set([start])
        path = {start: []}

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = (x + dx) % self.height , (y + dy) % self.length
                if (nx, ny) not in visited and self.board[nx][ny] != 1:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    path[(nx, ny)] = path[(x, y)] + [(dx, dy)]
                    if self.board[nx][ny] == 0:
                        return path[(nx, ny)]
        return None
    def __str__(self) -> str:
        return str(self.board)

if __name__ == "__main__":
    env = Env(18,9,2)
    env.board[4][4] = 1
    print(env.get_neighbors([4,4]))