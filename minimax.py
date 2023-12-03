import math
class Minimax:
    def __init__(self, game, depth):
        self.game = game
        self.depth = depth
        self.nodes = 0
        self.cache = {}

    def minimax(self, state, depth, maximizing_player):
        self.nodes += 1
        # if state in self.cache:
        #     return self.cache[state]
        if depth == 0 or state.is_terminal():
            # print(" >>>>>>>>> ",state.utility())
            a = state.utility()
            # print(a)
            return a
        if maximizing_player:
            value = -math.inf
            for child in state.successors(state):
                value = max(value, self.minimax(child, depth - 1, False))
            self.cache[state] = value
            return value
        else:
            value = math.inf
            for child in state.successors(state):
                value = min(value, self.minimax(child, depth - 1, True))
            self.cache[state] = value
            return value

    def get_action(self, state):
        best_value = -math.inf
        best_action = None
        for action in state.actions():
            value = self.minimax(state.result(action), self.depth - 1, False)
            if value > best_value:
                best_value = value
                best_action = action
                # print(f"best action: {action}")
        return best_action

    def get_nodes(self):
        return self.nodes

