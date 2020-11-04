import util
import game
import human
import agent

P1_C = 'X'
P2_C = 'O'
HUMAN = 'human'
RANDOM = 'random'
MINIMAX = 'minimax'
P_TYPES = [HUMAN, RANDOM, MINIMAX]


def players(p1_type, p2_type):
    '''players(p1_type, p2_type) -> (Player 1, Player 2)
    Determine what type of players p1 and p2 are and initialize them.'''
    # Initialize Player 1.
    if p1_type == HUMAN:
        player1 = human.HumanPlayer(P1_C)
    elif p1_type == RANDOM:
        player1 = agent.RandomPlayer(P1_C)
    elif p1_type == MINIMAX:
        player1 = agent.MinimaxPlayer(P1_C)

    # Initialize Player 2.
    if p2_type == HUMAN:
        player2 = human.HumanPlayer(P2_C)
    elif p2_type == RANDOM:
        player2 = agent.RandomPlayer(P2_C)
    elif p2_type == MINIMAX:
        player2 = agent.MinimaxPlayer(P2_C)

    return player1, player2

if __name__ == '__main__':
    p1_type = util.get_arg(1)
    p2_type = util.get_arg(2)
    if p1_type and p2_type and p1_type in P_TYPES and p2_type in P_TYPES:
        # Initialize Players and Game objects.
        player1, player2 = players(p1_type, p2_type)
        mygame = game.Game(player1, player2)

        # Play the game.
        winner, visted = mygame.play()
        
        # Print the winner.
        if winner:
            if winner == player1:
                print('Player 1 wins!')
            elif winner == player2:
                print('Player 2 wins!')
        else:
            print("It's a tie!")
            
        # Print entire sequence of state taken in game.
        util.pprint(visted)
