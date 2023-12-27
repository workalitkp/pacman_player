import logging
import copy
from abc import ABC, abstractmethod
import math
from random import shuffle
logger = logging.Logger("State", int(logging.INFO))
logger.addHandler(logging.FileHandler("state.log", mode="w"))
# from State import State
class State:
    def __init__(self, env, agent, ghost1, ghost2) -> None:
        '''
        Creates instances of the environment with agents and calculates the utility value for each state.
        The main use of this class is for the minimax algorithm.

        Args:
        - env: The environment object.
        - agent: The pacman agent object.
        - ghost1: The first ghost object.
        - ghost2: The second ghost object.
        '''
        self.env = env
        self.pacman = agent
        self.ghost1 = ghost1
        self.ghost2 = ghost2
        self.util = 0

    def utility(self):
        '''
        Calculates the utility value for the current state.

        Returns:
        - The utility value.
        '''
        x = self.pacman.pos[0]
        y = self.pacman.pos[1]
        pos = self.env.food[x][y]
        if self.pacman.pos == self.ghost1.pos or self.pacman.pos == self.ghost2.pos:
            self.util = -1000000000
        elif pos:
            self.util = 10
        else:
            self.util = -1
        logger.info(f"util-> : {self.util}")
        return self.util

    def conv(self, action):
        '''
        Converts the given action tuple to a string representation.

        Args:
        - action: The action tuple.

        Returns:
        - The string representation of the action.
        '''
        if action == (0, -1):
            return "left"
        elif action == (0, 1):
            return "right"
        elif action == (-1, 0):
            return "up"
        elif action == (1, 0):
            return "down"

    def actions(self):
        '''
        Returns a list of possible actions for the pacman agent.

        Returns:
        - The list of possible actions.
        '''
        actions = self.pacman.possible_moves(self.env)
        be = self.env.find_shortest_path(self.pacman.pos)[0]
        a = self.conv(be)
        actions.remove(a)
        actions = [a] + actions
        return actions

    def result(self, action):
        '''
        Applies the given action to the current state and returns the resulting state.

        Args:
        - action: The action to be applied.

        Returns:
        - The resulting state.
        '''
        self.env.step(self.pacman, action=action)
        return self

    def is_terminal(self):
        '''
        Checks if the current state is a terminal state.

        Returns:
        - True if the state is terminal, False otherwise.
        '''
        logger.log(int(logging.INFO), f"is_terminal: pacman: {self.pacman.pos}, ghost1: {self.ghost1.pos}, ghost2: {self.ghost2.pos}")
        if self.pacman.pos == self.ghost1.pos or self.pacman.pos == self.ghost2.pos:
            return True
        # check if any food left
        for i in range(self.env.height):
            for j in range(self.env.length):
                if self.env.board[i][j] == 0:
                    return False
        return True

    def successors(self):
        '''
        Generates a list of successor states for the current state.

        Returns:
        - The list of successor states.
        '''
        ab = []
        for action in self.actions():
            c_state = self.clone()
            ab.append(c_state.result(action))
        return ab

    @abstractmethod
    def clone(self):
        '''
        Creates a deep copy of the current state.

        Returns:
        - The cloned state object.
        '''
        return copy.deepcopy(self)
