import math
import logging

logger = logging.Logger("minimax", int(logging.INFO))
logger.addHandler(logging.FileHandler("minimax.log", mode="w"))

class Minimax:
    def __init__(self, game, depth):
        """
        Initializes a Minimax object.

        Parameters:
        - game: The game object.
        - depth: The depth of the search tree.

        Returns:
        None
        """
        self.game = game
        self.depth = depth
        self.nodes = 0
        self.cache = {}
        self.ut = 0

    def minimax(self, state, depth, player, alpha, beta):
        """
        Implements the minimax algorithm.

        Parameters:
        - state: The current state of the game.
        - depth: The current depth of the search tree.
        - player: The player making the move (0 for max player, 1 and 2 for min players).
        - alpha: The alpha value for alpha-beta pruning.
        - beta: The beta value for alpha-beta pruning.

        Returns:
        The utility value of the state.
        """
        self.nodes += 1
        if depth == 0 or state.is_terminal():
            self.ut = state.utility()
            return self.ut

        if player == 0:  # max player
            value = -math.inf
            for child in state.successors():
                value = max(value, self.minimax(child, depth - 1, (player + 1) % 3, alpha, beta))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else: 
            value = math.inf
            for child in state.successors():
                value = min(value, self.minimax(child, depth - 1, (player + 1) % 3, alpha, beta))
                beta = min(beta, value)
                if beta <= alpha:
                    break  
            return value

    def get_action(self, state):
        """
        Returns the best action to take based on the current state.

        Parameters:
        - state: The current state of the game.

        Returns:
        The best action to take.
        """
        best_value = -math.inf
        best_action = None

        for action in state.actions():
            c_state = state.clone()
            value = self.minimax(c_state.result(action), self.depth, 0, -math.inf, math.inf)
            if value > best_value:
                best_value = value
                best_action = action
                logger.log(int(logging.INFO),f"best action: {action}")
        return best_action

    def get_nodes(self):
        """
        Returns the number of nodes expanded during the search.

        Parameters:
        None

        Returns:
        The number of nodes expanded.
        """
        return self.nodes



