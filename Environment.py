from collections import deque
import random
import math
class Env:
    def __init__(self, length, height, difficulty=1) -> None:
        '''
        Initializes the environment with the specified length, height, and difficulty.

        Parameters:
        - length (int): The length of the environment.
        - height (int): The height of the environment.
        - difficulty (int, optional): The difficulty level of the environment. Defaults to 1.

        Attributes:
        - length (int): The length of the environment.
        - height (int): The height of the environment.
        - board (list): The game board represented as a 2D list.
        - food (list): The food positions represented as a 2D list.
        - difficulty (int): The difficulty level of the environment.
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
        '''
        Inserts the agent into the environment.

        Parameters:
        - agent (Agent): The agent to be inserted.
        '''
        if agent.type == 2:
            self.board[agent.pos[0]][agent.pos[1]] = 2
        else:
            if(self.board[agent.pos[0]][agent.pos[1]]) == 4:
                self.board[agent.pos[0]][agent.pos[1]] = 3

            elif(self.board[agent.pos[0]][agent.pos[1]] == 0):
                self.board[agent.pos[0]][agent.pos[1]] = 5

    def remove_agent(self, agent):
        '''
        Removes the agent from the environment.

        Parameters:
        - agent (Agent): The agent to be removed.
        '''
        if agent.type==3:
            if self.board[agent.pos[0]][agent.pos[1]] == 5:
                self.board[agent.pos[0]][agent.pos[1]] = 0
            else:
                self.board[agent.pos[0]][agent.pos[1]] = 4
        else:
            self.board[agent.pos[0]][agent.pos[1]] = 4

    def step(self, agent, action):
        '''
        Takes a step in the environment based on the agent's action.

        Parameters:
        - agent (Agent): The agent taking the step.
        - action (str): The action to be taken by the agent.

        Returns:
        - self (Env): The updated environment after the step.
        '''
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
        score = -1
        if self.is_food(agent.pos):
            score = 10
        self.insert_agent(agent)
        return self,score

    def is_wall(self, coord):
        '''
        Checks if the given coordinate is a wall.

        Parameters:
        - coord (tuple): The coordinate to be checked.

        Returns:
        - bool: True if the coordinate is a wall, False otherwise.
        '''
        if self.board[coord[0]][coord[1]] == 1:
            return True
        return False

    def is_food(self, coord):
        '''
        Checks if the given coordinate has food.

        Parameters:
        - coord (tuple): The coordinate to be checked.

        Returns:
        - bool: True if the coordinate has food, False otherwise.
        '''
        if self.board[coord[0]][coord[1]] == 0:
            return True
        return False

    def is_ghost(self, coord):
        '''
        Checks if the given coordinate has a ghost.

        Parameters:
        - coord (tuple): The coordinate to be checked.

        Returns:
        - bool: True if the coordinate has a ghost, False otherwise.
        '''
        if self.board[coord[0]][coord[1]] == 5:
            return True
        return False

    def find_shortest_path(self, start):
        '''
        Finds the shortest path from the given start coordinate to the nearest food.

        Parameters:
        - start (tuple): The starting coordinate.

        Returns:
        - list or None: The shortest path as a list of directions (dx, dy) or None if no path is found.
        '''
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
        '''
        Returns a string representation of the environment.

        Returns:
        - str: The string representation of the environment.
        '''
        return str(self.board)

if __name__ == "__main__":
    env = Env(18,9,2)
    env.board[4][4] = 1
