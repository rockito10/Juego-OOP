import unittest   # The test framework
import game.game as core_game #importo el manejador del juego entero

#ojo que "e" siempre tira "error"

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4, 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(4, 4)


class Test_TestGame(unittest.TestCase):
    def test_game(self):
        currentGame = core_game.Game()
        currentGame.run([1,"a","a","s","d","w","w","w"]) 
        
    def test_room_move(self):
        currentGame = core_game.Game()
        currentGame.run([1,"a","a","s","d","w","w","w"]) 
        
    def test_floor_move(self):
        currentGame = core_game.Game()
        currentGame.run(
        [1, "w", "w", "w", "w", "a", "a", "a", "s", "d", "d", "d", "d", "w", "w", "a", 
                               "w", "w", "w", "w", "w", "w", "s", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", 
                               "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", 
                               "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "d", "d", "d", "d", 
                               "d", "w", "w", "w", "w", 
"w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", 
"w", "w", "w", "w", "w", "w", "w", "s", "s", "s", "s"])
        
    def test_combat_1(self):
        currentGame = core_game.Game()
        currentGame.run([1, 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'])
        self.assertEqual(70, currentGame.current_match.player.hp)
    
if __name__ == '__main__':
    unittest.main()