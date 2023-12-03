class State:
    def __init__(self, env,agent,ghost1,ghost2) -> None:
        self.env = env
        self.pacman = agent
        self.ghost1 = ghost1
        self.ghost2 = ghost2
        self.util = 0
    def utility(self):
        if self.pacman.pos == self.ghost1.pos or self.pacman.pos == self.ghost2.pos:
            self.util += -100
            # return self.util 
        elif self.env.board[self.pacman.pos[0]][self.pacman.pos[1]] == 0:
            self.util += 10
            # return self.util
        else:
            self.util += 0
        return self.util

    def actions(self):
        return ["left", "right", "up", "down"]

    def result(self,action):
        if action == "right":
            self.pacman.pos[1] = (self.pacman.pos[1] + 1) % self.env.length
        elif action == "left":
            self.pacman.pos[1] = (self.pacman.pos[1] - 1) % self.env.length
        elif action == "down":
            self.pacman.pos[0] = (self.pacman.pos[0] + 1) % self.env.height
        elif action == "up":
            self.pacman.pos[0] = (self.pacman.pos[0] - 1) % self.env.height
        self.env.step(agent=self.pacman,action=action)
        return self
    def is_terminal(self):
        if self.pacman.pos == self.ghost1.pos or self.pacman.pos == ghost2.pos:
            return True
        # check if any food left
        for i in range(self.env.height):
            for j in range(self.env.length):
                if self.env.board[i][j] == 0:
                    return False
        return True
    def successors(self,env):
        ab = [self.result(action) for action in self.actions()]
        # print(ab)
        return ab 
