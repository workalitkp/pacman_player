import logging
import copy
from abc import ABC, abstractmethod
import math
from random import shuffle
logger = logging.Logger("State", int(logging.INFO))
logger.addHandler(logging.FileHandler("state.log", mode="w"))
# from State import State
class State:
    def __init__(self, env,agent,ghost1,ghost2) -> None:
        '''creates instances of env with agents and calcs util value for each state -> main use is for minimax'''
        self.env = env
        self.pacman = agent
        self.ghost1 = ghost1
        self.ghost2 = ghost2
        self.util = 0
    def utility(self):
        x = self.pacman.pos[0]
        y = self.pacman.pos[1]
        pos = self.env.food[x][y]
        if self.pacman.pos == self.ghost1.pos or self.pacman.pos == self.ghost2.pos:
            self.util = -1000000000
            # logger.log(int(logging.INFO),f"pacman: {self.pacman.pos}, ghost1: {self.ghost1.pos}, ghost2: {self.ghost2.pos}, util: {self.util}")

            # return self.util 
        elif pos:
            self.util = 10
            self.env.food[x][y] = 0
            # return self.util
        else:
            self.util = -1
        logger.info(f"util-> : {self.util}")
        return self.util

    def actions(self):
        actions = self.pacman.possible_moves(self.env)
        shuffle(actions)
        return actions

    def result(self,action):
        self.env.step(self.pacman,action=action)
        return self
    def is_terminal(self):
        logger.log(int(logging.INFO),f"is_terminal: pacman: {self.pacman.pos}, ghost1: {self.ghost1.pos}, ghost2: {self.ghost2.pos}")
        if self.pacman.pos == self.ghost1.pos or self.pacman.pos == self.ghost2.pos:
            return True
        # check if any food left
        for i in range(self.env.height):
            for j in range(self.env.length):
                if self.env.board[i][j] == 0:
                    return False
        return True
    def successors(self):
        ab = []
        for action in self.actions():
            c_state = self.clone()
            ab.append(c_state.result(action))
        return ab
    @abstractmethod
    def clone(self):
        return copy.deepcopy(self)
