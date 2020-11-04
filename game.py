import connect3
import util


class Player:

    def __init__(self, char):
        self.char = char

    def choose_action(self, state):
        '''choose_action(state) -> action
        Choose an action based on the current state of the game.'''

        raise NotImplementedError


class Game:

    def __init__(self, player1=Player('X'), player2=Player('O')):
        self.player1 = player1
        self.player2 = player2
        self.state = None

    def play(self):
        '''play() -> (winning player, visited states)
        Start from an initially blank board and alternate between players.
        Ask each player to choose an action and then update the game state.
        Return a tuple of the winning player or None if the no winner and the
        board is full and a list of the visited states.'''

        visited = []
        self.state = connect3.State()

        # Loop until game is won or board is full.
        while not self.state.game_over():
            # Execute player's action and update board state.
            self.update(self.player1, visited)

            if not self.state.game_over():
                self.update(self.player2, visited)
            else:
                break

        # Get winning player based on the winning character (X or O).
        winning_c = self.state.winner()
        if winning_c:
            if winning_c == self.player1.char:
                winner = self.player1
            elif winning_c == self.player2.char:
                winner = self.player2
        else:
            winner = None

        return (winner, visited)

    def update(self, player, visited):
        '''update(player, visited)
        Get a player's chosen action, execute that action on the board state,
        print record the result.'''

        action = player.choose_action(self.state)
        self.state.execute(action)
        util.pprint(self.state)
        visited.append(self.state.clone())
