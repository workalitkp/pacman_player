class Agent:
    def __init__(self, type, pos) -> None:
        if type == "pacman":
            self.type = 2
            self.pos = pos
        elif type == "ghost":
            self.type = 3
            self.pos = pos
    def possible_moves(self,env):
        '''returns moves that do not cause agent to hit a wall'''
        moves = ['right','left','down','up']
        possible_moves = []
        for action in moves:
            match action:
                case "right":
                    if not env.is_wall([self.pos[0],((self.pos[1] + 1) % env.length)]):
                        possible_moves.append('right')
                case "left":
                    if not env.is_wall([self.pos[0],((self.pos[1] + 1) % env.length)]):
                        possible_moves.append('left')
                case "down":
                    if not env.is_wall([self.pos[0],((self.pos[1] + 1) % env.length)]):
                        possible_moves.append('down')
                case "up":
                    if not env.is_wall([self.pos[0],((self.pos[1] + 1) % env.length)]):
                        possible_moves.append('up')
        return possible_moves
    def closest_food(self, env):
        """
        Returns the move towards the closest food using DFS.

        Args:
            env (Environment): The game environment.

        Returns:
            str: The move towards the closest food.
        """
        stack = [(self.pos, [])]
        visited = set()

        while stack:
            (node, path) = stack.pop()
            if env.is_food(node):
                return path[0] if path else None
            if tuple(node) not in visited:
                visited.add(tuple(node))
                for move, new_node in env.get_neighbors(node):
                    stack.append((new_node, path + [move]))

        return None
    def __str__(self) -> str:
        return f"{self.type} >  {self.pos}"
    