def game(player1, player2):
    """
    Enter values that present the player choice
    Return p1 if player 1 wins otherway p2
    """
    if (player1 == 'r' and player2 == 'r') or (player1 == 's' and player2 == 's') or (player1 == 'p' and player2 == 'p'):
        return 'EMPATE'
    if player1 == 'r' or player2 == 's' :
        return 'Rock Wins'
    if player1 == 's' or player2 == 'p' :
        return 'Scissors Wins'
    if player1 == 'p' or player2 == 'r' :
        return 'Paper Wins'

