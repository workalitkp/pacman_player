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
                    if not env.is_wall([self.pos[0],(self.pos[1] + 1) % env.length]):
                        possible_moves.append(action)
                case "left":
                    if not env.is_wall([self.pos[0],(self.pos[1] - 1) % env.length]):
                        possible_moves.append(action)
                case "down":
                    if not env.is_wall([(self.pos[0] + 1) % env.height,self.pos[1]]):
                        possible_moves.append(action)
                case "up":
                    if not env.is_wall([(self.pos[0] - 1) % env.height,self.pos[1]]):
                        possible_moves.append(action)
        return possible_moves
    def __str__(self) -> str:
        return f"{self.type} >  {self.pos}"
    