from game import Player

class HumanPlayer(Player):

    def __init__(self, char):
        super().__init__(char)

    def choose_action(self, state):
        '''choose_action(state) -> action
        Determine the possible actions from the given state and print the
        index and the action. Then present the user with the option to select
        one of the actions.'''

        # Print the Players possible actions.
        actions = state.actions(self.char)
        num_actions = len(actions)
        for i in range(num_actions):
            print(f'{i}: {actions[i]}')

        while True:
            # Get Human's choice.
            choice = input('Please choose an action: ')

            try:
                choice_i = int(choice)

                # Test choice is in range.
                if choice_i in range(num_actions):
                    break
                else:
                    raise ValueError

            except ValueError:
                print(f'Enter number 0-{num_actions-1}')

        return actions[choice_i]