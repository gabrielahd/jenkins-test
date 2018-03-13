from game import game
def test_game_01():
    assert game ('r', 's') == 'Rock Wins', 'Rocks should win'
    assert game ('s', 'p') == 'Scissors Wins', 'Scissor should win'
    assert game ('p', 'r') == 'Paper Wins', 'Paper should win'


test_game_01();
    
