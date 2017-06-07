"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer(score_fn=game_agent.custom_score)        
        self.player2 = game_agent.AlphaBetaPlayer(score_fn=game_agent.custom_score)        
        self.game = isolation.Board(self.player1, self.player2)
        print("player1:",self.player1)
        print("player2:",self.player2)
        
    def test_MiniMaxPlayer(self):
        self.game.apply_move((2,3))
        self.game.apply_move((0,0))
        assert(self.player1==self.game.active_player)
        print(self.game.to_string())
        #print(self.game.get_legal_moves())
        winner, history, outcome=self.game.play()
        print(history)
        print("winner is {0} with outcome {1}".format(winner,outcome))
        print(self.game.to_string())
        #game_copy=self.game.copy()
        #curr_move = self.player1.get_move(game_copy, time_left)


if __name__ == '__main__':
    unittest.main()
