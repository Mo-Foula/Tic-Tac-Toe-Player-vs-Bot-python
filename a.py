class Move:
    def __init__(self, row, col):
        self.row = row
        self.col = col
import random

# Main Program
import math as Math



class GameInitializationRules:
    def __init__(self, botChar='x', playerChar='o', blankSpace='_', unitScore=10):
        self.bot = botChar
        self.player = playerChar
        self.blankSpace = blankSpace
        self.uniCorn = unitScore

    def get_botChar(self):
        return self.bot

    def get_playerChar(self):
        return self.player

    def get_blankSpace(self):
        return self.blankSpace

    def get_unitScore(self):
        return self.uniCorn


playerOBBBBj = GameInitializationRules(botChar='x', playerChar='o', blankSpace='_', unitScore=10)

# def koko(z):
#     print(z.get_botChar())
# koko(playerOBBBBj)

# Bot = 'x'
# Player = 'o'
# blankSpace = '_'
# # unit score
# unitCorn = 10


# movesleft?
def isThereAnyMovesLeftPleaseAnswerQuicklyMeshAderAtnfsناو(board, gameObject):
    blankSpace = gameObject.get_blankSpace()
    for i in board:
        for j in i:
            if j is blankSpace:
                return True
    return False


# evaluation
def yataraFe7adKasab(board, gameObject = GameInitializationRules()):
    Bot = gameObject.get_botChar()
    Player = gameObject.get_playerChar()
    unitCorn = gameObject.get_unitScore()

    # check if there's a winner in a row
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] is Bot:
                return unitCorn
            elif row[0] is Player:
                return -unitCorn

    #  check if there's a winner in a column
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] is Bot:
                return unitCorn
            elif board[0][col] is Player:
                return -unitCorn

    # check if there's a winner in a diagonal
    # 1st diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] is Bot:
            return unitCorn
        elif board[0][0] is Player:
            return -unitCorn
    # 2nd diagonal
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if board[0][2] is Bot:
            return unitCorn
        elif board[0][2] is Player:
            return -unitCorn

    # No winner yet
    return 0


def minimax(board, depth, isMax, gameObject = GameInitializationRules()):
    Bot = gameObject.get_botChar()
    Player = gameObject.get_playerChar()
    blankSpace = gameObject.get_blankSpace()

    score = yataraFe7adKasab(board, gameObject=gameObject)

    # check if player or opponent won the game
    if score == 10:
        return score - depth
        # return score
    elif score == -10:
        return score + depth
        # return score

    # if reached here then no one won yet

    # if no moves left, end with a draw
    if not isThereAnyMovesLeftPleaseAnswerQuicklyMeshAderAtnfsناو(board, gameObject=gameObject):
        return 0

    # hngrab nshof a7san tare2 (best value)
    if isMax:
        # Maximized (Bot's) turn

        bestValue = float('-inf')
        # bestValue = -1000

        for row in range(3):
            # for char in row:
            for col in range(3):
                if board[row][col] == blankSpace:
                    # hangrab b2a lw hnl3b hena
                    board[row][col] = Bot

                    # hankml el game w el door yb2a 3la opponent
                    # not isMax 34an a switch el player
                    bestValue = max(bestValue, minimax(board, depth + 1, not isMax, gameObject=gameObject))

                    # undo the move
                    board[row][col] = blankSpace
        return bestValue

    else:
        # Player's turn (minimization)
        bestValue = float('inf')
        # bestValue = 1000
        for row in range(3):
            # for char in row:
            for col in range(3):
                if board[row][col] == blankSpace:
                    # hangrab b2a lw hnl3b hena
                    board[row][col] = Player

                    # hankml el game w el door yb2a 3la opponent
                    # not isMax 34an a switch el player
                    bestValue = min(bestValue, minimax(board, depth + 1, not isMax, gameObject=gameObject))

                    # undo the move
                    board[row][col] = blankSpace
        return bestValue


# findBestMove
def a7laMove3lek(board, gameObject = GameInitializationRules()):
    Bot = gameObject.get_botChar()
    Player = gameObject.get_playerChar()
    unitCorn = gameObject.get_unitScore()
    blankSpace = gameObject.get_blankSpace()
    # el bot bnsbalna maxmizer
    # assuming im calculating the best move for the BOT (maxmization)
    bestValue = float('-inf')
    # bestValue = -1000
    bestMove = Move(row=-1, col=-1)

    moveValue = 0

    for row in range(0, 3):
        for col in range(3):
            # char = board[row][col]

            if board[row][col] == blankSpace:
                board[row][col] = Bot

                moveValue = minimax(board, 0, False, gameObject=gameObject)

                board[row][col] = blankSpace

                # > 34an bagib max (BOT)
                if moveValue > bestValue:
                    bestValue = moveValue
                    bestMove.col = col
                    bestMove.row = row

    return bestMove


# Bot Turn
def el3abYaaa(board, gameObj = GameInitializationRules()):
    Bot = gameObj.get_botChar()
    bestMove = a7laMove3lek(board, gameObject=gameObj)
    board[bestMove.row][bestMove.col] = Bot
    return board


def printBoard(board, gameObj = GameInitializationRules()):
    Bot = gameObj.get_botChar()
    Player = gameObj.get_playerChar()

    print('-------------')
    for r in board:
        for c in r:
            if c == Bot:
                print(f'| {c} ', end='')
            elif c == Player:
                print(f'| {c} ', end='')
            else:
                print(f'| {c} ', end='')
        print('|\n-------------')


def takeInput(board, gameObj = GameInitializationRules()):

    Bot = gameObj.get_botChar()
    Player = gameObj.get_playerChar()
    blankSpace = gameObj.get_blankSpace()

    while True:
        i = 1
        print('-------------')
        for r in board:
            for c in r:
                if c == blankSpace:
                    print(f'| {i} ', end='')
                elif c == Bot:
                    print(f'| {c} ', end='')
                else:
                    print(f'| {c} ', end='')
                i += 1
            print('|\n-------------')

        print('Please enter the number you want to play into')
        inp = int(input())
        inpCol = ((inp % 3) + 2) % 3
        inpRow = Math.floor((inp - 1) / 3)
        if inp >= 1 and inp <= 9 and board[inpRow][inpCol] == blankSpace:
            board[inpRow][inpCol] = Player
            break
        else:
            print('Enter a valid number')

    return board


def choosePlayerSymbol():
    print('Please choose your symbol \'x\' or \'o\'')
    while True:
        char = input()
        if char == 'x':
            return 'x'
        if char == 'o':
            return 'o'
        print('Please choose x or o only')


def resetBoard():
    return [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def simulateGame():

    # MAIN
    char = choosePlayerSymbol()
    Bot = 'x'
    Player = 'o'
    # player is the opponent in the game and the bot is the player
    if char == 'x':
        Bot = 'o'
        Player = 'x'

    # The rest are the default
    gameObject = GameInitializationRules(botChar=Bot, playerChar=Player)

    stopPlaying = False
    check = False

    board = resetBoard()
    #
    isPlayerTurn = True
    ccc = random.randint(0, 2)
    if ccc == 0:
        isPlayerTurn = False
    while not stopPlaying:
        if isPlayerTurn:
            board = takeInput(board, gameObj=gameObject)
        else:
            board = el3abYaaa(board, gameObj=gameObject)

        check = yataraFe7adKasab(board, gameObject=gameObject)

        if check != 0:
            stopPlaying = True
            if check == 10:
                print(f'YOU LOST!')
            else:  # -10
                print(f'YOU WON!')

        elif not isThereAnyMovesLeftPleaseAnswerQuicklyMeshAderAtnfsناو(board, gameObject=gameObject):
            # Draw
            stopPlaying = True
            print(f'DRAW!')
        else:
            # lsa m7dsh kasab
            isPlayerTurn = not isPlayerTurn

    printBoard(board, gameObj=gameObject)
    return check




    # root = Tk()
    # canvas = Canvas(root, width=500, height=500)
    # canvas.pack()
    # img = ImageTk.PhotoImage(Image.open("Saw33.jpg"))
    # canvas.create_image(20, 20, anchor=NW, image=img)
    # root.mainloop()
# import timg
#
# obj = timg.Renderer()
# obj.load_image_from_file("test.png")
# obj.resize(100,40)
# obj.render(timg.ASCIIMethod)

# el Main el 7a2e2i

print('      I WANNA PLAY A GAME')
print('YOU HAVE TO WIN AGAINST THE HARDEST BOT')
botscore = 0
playerscore = 0
check = True
while check:
    score = simulateGame()
    if score > 0:
        botscore += 1
    elif score < 0:
        playerscore += 1

    print('Total Score is', playerscore-botscore)
    a = input('Do you want to continue? (enter if yes, write \'n\' or \'no\' if no)')
    if a == 'n' or a == 'no':
        check = False


if botscore > playerscore:
    print('GAME OVER')
else:
    print('CONGRATULATIONS YOU ARE STILL ALIVE\n\tYOU HAVE BEEN REBIRTHED')
# Testing

# board = [['x', 'x', 'o'],
#          ['_', 'x', 'o'],
#          ['_', '_', 'x']]
# printBoard(takeInput(board))
# board = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# board = [['x', 'o', 'o'],
#          ['_', 'o', 'x'],
#          ['x', '_', '_']]
