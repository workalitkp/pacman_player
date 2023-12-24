import math
import logging

logger = logging.Logger("minimax", int(logging.INFO))
logger.addHandler(logging.FileHandler("minimax.log", mode="w"))

class Minimax:
    def __init__(self, game, depth):
        self.game = game # game is unnec
        self.depth = depth
        self.nodes = 0
        self.cache = {}
        self.ut = 0

    def minimax(self, state, depth, player):
        """
        Applies the minimax algorithm to determine the best move for the current player.

        Parameters:
        - state: The current state of the game.
        - depth: The depth of the search tree.
        - maximizing_player: A boolean indicating whether the current player is maximizing or not.

        Returns:
        - The utility value of the best move for the current player.

        player: 0 for max player, 1 and 2 for min players
        """
        self.nodes += 1
        # if state in self.cache:
        #     return self.cache[state]
        if depth == 0 or state.is_terminal():
            self.ut = state.utility()
            # logger.log(int(logging.INFO),f"util: {self.ut},{depth}")
            return self.ut
        
        if player==0:
            value = -math.inf
            a = state.successors()
            for child in a:
                aa = self.minimax(child, depth - 1,(player + 1) % 3)
                value = max(value, aa)
            # self.cache[state] = value
            return value
        else:
            value = math.inf
            for child in state.successors():
                value = min(value, self.minimax(child, depth - 1,(player + 1) % 3))
            # self.cache[state] = value
            return value

    def get_action(self, state):
        best_value = -math.inf
        best_action = None
        utility_values = []

        for action in state.actions():
            c_state = state.clone()
            value = self.minimax(c_state.result(action), self.depth - 1,0)
            if value > best_value:
                best_value = value
                best_action = action
                logger.log(int(logging.INFO),f"best action: {action}")
        return best_action

    def get_nodes(self):
        return self.nodes



