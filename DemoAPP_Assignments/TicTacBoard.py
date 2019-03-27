def TicTacTestBoard(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def SetTicTacBoard():
    board=['','','','','','','','','','']
    Player1Marker=input(" Enter your choice X or O: ")
    if Player1Marker=='X'.upper():
        Player2Marker='O'
    else:
        Player2Marker='X'
    def PrintBoard():
        print(board[7] + '|' + board[8] + '|' + board[9])
        print(board[4] + '|' + board[5] + '|' + board[6])
        print(board[1] + '|' + board[2] + '|' + board[3])

    def playGame(board,Player1Marker, Player2Marker):
        while (board[1] == board[2] == board[3] != 'X' or board[1] == board[2] == board[3] != 'O' or board[4] == board[
            5] == board[6] != 'X' or board[4] == board[5] == board[6] != 'O' or board[7] == board[8] == board[
                   9] != 'X' or board[7] == board[8] == board[9] != 'O' or board[3] == board[5] == board[7] != 'X' or
               board[
                   3] == board[5] == board[7] != '0' or board[1] == board[5] == board[9] != 'X' or board[1] == board[
                   5] ==
               board[9] != 'O'):
            player1=int(input("player 1 enter ur step between 1-9:"))
            board[player1]=Player1Marker
           # board.insert(player1,Player1Marker)
            PrintBoard()
            player2=int(input("player 2 enter ur step between 1-9:"))
            board[player2] = Player2Marker
           # board.insert(player2,Player2Marker)
            PrintBoard()
        if(board[1] == board[2] == board[3] == 'X' or board[4] == board[5] == board[6] == 'X' or board[7] == board[8] == board[9] == 'X' or board[3] == board[5] == board[7] == 'X' or board[1] == board[5] == board[9] == 'X'):
            if(Player1Marker=='X'):
                print("Congratulations:Player1, You Won the Game")
            else:
                print("Congratulations:Player2, You Won the Game")
        else:
            if(Player1Marker=='O'):
                print("Congratulations:Player1, You Won the Game")
            else:
                print("Congratulations:Player2, You Won the Game")

    playGame(board,Player1Marker, Player2Marker)
    playagain=input("Do u want to play again?")
    if(playGame.upper()=='YES'):
        playGame(board, Player1Marker, Player2Marker)
    else:
        print('Thanks for playing, Have A Great Day')


SetTicTacBoard()