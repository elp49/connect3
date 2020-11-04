from game import Player
import random

class RandomPlayer(Player):

    def __init__(self, char):
        super().__init__(char)

    def choose_action(self, state):
        '''choose_action(state) -> action
        Choose a random action of the possible actions on the given state.'''

        actions = state.actions(self.char)

        rand_i = random.randint(0, len(actions) - 1)

        return actions[rand_i]


class MinimaxPlayer(Player):
    FIXED_DEPTH = 3

    def __init__(self, char):
        super().__init__(char)

    def choose_action(self, state):
        '''choose_action(state) -> action
        Use the minimax algorithm to choose an action.'''

        actions = state.actions()
        num_actions = len(actions)

        # Base Case: Check if only one action.
        if num_actions == 1:
            return actions[0]

        # Check if any actions result in win.

        # Execute each action on cloned curret state and record result state.
        results = []
        for a in actions:
            clone = state.clone()
            clone.execute(a)
            results.append(clone)

        for i in range(len(results)):
            # If action results in a win return it.
            if results[i].winner() == self.char:
                return actions[i]



        raise NotImplementedError

    def evaluate(self):
        '''The evaluation funtion that assigns a value to any final game states.'''

        # Note that it’s a good idea to also include diminishing returns for
        # nodes deeper in the tree, thus giving higher values for nodes with
        # shorter paths.

        raise NotImplementedError