## Kate Christensen - Tic Tac Toe Game - CSE 210

##The program must have at least one while loop.

def main():
## main function for the program   

    def intro():
        ## Introducing the rules of the game and the players
        print("\n")
        print("Hello and welcome to the game Tic Tac Toe!")
        print("The first player will be X's and second player will be O's.")
        print("Winning the game is accomplished by getting three of your tokens in a row, either vertical, horizontal or diagonal.")
        print("\n")
        print("Here is the board layout: ")
        print("1" + '|' +"2" + '|' + "3")
        print('-+-+-')
        print("4" + '|'+"5"+'|'+"6")
        print('-+-+-')
        print("7"+'|' + "8" + '|' + "9")
        print("Ready to play?")
        print("\n")
    intro()
    
    board = { '1': ' ', '2':' ', '3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
    board_keys = []

    for key in board:
        board_keys.append(key)
        
    def printBoard(board):
        ## Establishing the Tic Tac Toe board
       
        print(board['1']+ '|'+ board ['2']+ '|' + board['3'])
        print('-+-+-')
        print(board['4']+ '|'+board['5']+'|'+board['6'])
        print('-+-+-')
        print(board['7']+'|'+ board['8']+ '|'+ board['9'])
    

    def playGame():
        ## Function for actual game play
        count = 0
        turn = "X"

        for i in range(10):
            printBoard(board)
            print("It's your turn, "+ turn + ". Which space would you like?")

            move = input()
                
            if board[move] == ' ':
                board[move] = turn
                count += 1
            else:
                print("That place is filled.\nWhat is your next choice?")
                continue

            if count >= 5:
                if board['7'] == board['8'] == board['9'] != ' ': 
                    printBoard(board)
                    print("Game Over!")
                    print(turn +" wins!")
                    break
                elif board['4'] == board['5'] == board ['6'] != ' ':
                    printBoard(board)
                    print("Game Over!")
                    print(turn + " wins!")
                    break
                elif board['1'] == board['2'] == board ['3'] != ' ':
                    printBoard(board)
                    print("Game Over!")
                    print(turn + " wins!")
                    break
                elif board['1'] == board['4'] == board ['7'] != ' ':
                    printBoard(board)
                    print("Game Over!")
                    print(turn + " wins!")
                    break
                elif board['2'] == board['5'] == board ['8'] != ' ':
                    printBoard(board)
                    print("Game Over!")
                    print(turn + " wins!")
                    break
                elif board['3'] == board['6'] == board ['9'] != ' ':
                    printBoard(board)
                    print("Game Over!")
                    print(turn + " wins!")
                    break
                elif board['7'] == board['5'] == board ['3'] != ' ':
                    printBoard(board)
                    print("Game Over!")
                    print(turn + " wins!")
                    break
                elif board['1'] == board['5'] == board ['9'] != ' ':
                    printBoard(board)
                    print("Game Over!")
                    print(turn + " wins!")      
                    break                  
            if count == 9:
                print("Game Over! It's a tie!")            

            if turn == "X":
                turn = "O"
            else:
                turn = "X"
    playGame()     
    
    while True:
        answer = input("Would you like to play again?(y/n)")
        if answer == 'y' or answer == 'Y':
            intro()
            printBoard(board)
            playGame()
        elif answer == 'n' or answer == 'N':
            print("Thank you for playing!")
            break

main()
