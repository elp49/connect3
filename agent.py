from game import Player
import random
import math
from connect3 import Cell

class RandomPlayer(Player):

    def __init__(self, char):
        super().__init__(char)

    def choose_action(self, state):
        '''choose_action(state) -> action
        Choose a random action of the possible actions on the given state.'''

        # Choose a random action.
        actions = state.actions(self.char)
        rand_i = random.randint(0, len(actions) - 1)
        return actions[rand_i]


class MinimaxPlayer(Player):

    def __init__(self, char):
        super().__init__(char)

    def choose_action(self, state):
        '''choose_action(state) -> action
        Use the Minimax algorithm and Alpha-Beta Pruning to choose an action.'''

        actions = state.actions(self.char)

        # Base Case: Check if only one action.
        if len(actions) == 1:
            return actions[0]

        # Get resulting states of each action on current state.
        children = []
        for a in actions:
            clone = state.clone()
            clone.execute(a)
            children.append(clone)

        # Check if any actions result in win.
        for i in range(len(children)):
            # If action results in a win return action.
            if children[i].winner() == self.char:
                return actions[i]

        # Use minimax algorithm to evalutate best action.
        child_values = []
        for c in children:
            child_values.append(self.minimax(c, 12, False, -math.inf, math.inf))

        return actions[child_values.index(max(child_values))]

    def minimax(self, state, depth, is_players_turn, alpha, beta):
        '''choose_action(state, depth, is_players_turn, alpha, beta) -> action
        The Minimax algorithm with Alpha-Beta Pruning.'''

        # Base Case: Test if max depth is reached or if the game is over.
        if depth == 0 or state.game_over():
            return self.evaluate(state, is_players_turn)

        # Get resulting states of each action on current state.
        children = state.children(self.char)

        depth -= 1
        if is_players_turn:
            # Initialize a maximum value.
            max_val = -math.inf
            for c in children:
                # Determine the evaluation value of child.
                val = self.minimax(c, depth, False, alpha, beta)

                # Test if child value is greater than max.
                max_val = max(max_val, val)

                # Test if branches can be pruned.
                alpha = max(alpha, val)
                if beta <= alpha:
                    break

            return max_val

        else:
            # Initialize a minimum value.
            min_val = math.inf
            for c in children:
                # Determine the evaluation value of child.
                val = self.minimax(c, depth, True, alpha, beta)
                
                # Test if child value is less than max.
                min_val = min(min_val, val)
                
                # Test if branches can be pruned.
                beta = min(beta, val)
                if beta <= alpha:
                    break

            return min_val

    def evaluate(self, state, is_players_turn):
        '''evaluate(state, is_players_turn) -> evalutation value of state
        The evaluation funtion that assigns a value game states.'''

        count = 0
        for x in range(state.max_x):
            for y in range(state.max_y):
                c = state.get(x, y)
                if c != Cell.EMPTY:
                    deltas = [(+1, 0), (0, +1), (+1, +1), (-1, +1)]
                    for dx, dy in deltas:
                        count += self.get_state_val(state, is_players_turn, c, x, y, dx, dy)

        return count


    def get_state_val(self, state, is_players_turn, c, x, y, dx, dy):
        val = 0
        for _ in range(state.connect - 1):
            x += dx
            y += dy

            # Get the next character.
            next_c = state.get(x, y)

            # Test if next character is same as the first char or is Empty.
            if next_c == c or next_c == Cell.EMPTY:
                # Test if character is this Player's.
                if c == self.char:
                    if is_players_turn:
                        val += 1
                    else:
                        val -= 5
                else:
                    if is_players_turn:
                        val -= 5
                    else:
                        val += 1

        return val
