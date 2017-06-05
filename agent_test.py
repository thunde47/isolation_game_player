"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload

def time_left():
    return 1000000
class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        
    def test_MiniMaxPlayer(self):
        
        
        self.game.apply_move((4,4))
        self.game.apply_move((0,1))
        assert(self.player1 == self.game.active_player)
        isolation_player_object=game_agent.IsolationPlayer()
        game_agent_object=game_agent.MinimaxPlayer(isolation_player_object)
        new_move=game_agent.MinimaxPlayer.get_move(game_agent_object, self.game,time_left)
        
        print(self.game.to_string())


if __name__ == '__main__':
    unittest.main()
