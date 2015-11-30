import csplot
import random
from time import sleep

class ConnectFour:
    """ Class representing the game Connect Four. """

    # Represent different values on the board
    FREE = 0
    PLAYER1 = 1
    PLAYER2 = 2
    
    # Represent the dimensions of the board
    ROWS = 6
    COLS = 7

    # dictionary of number-->color mappings
    repToColor = {FREE:'yellow', PLAYER1:'red', PLAYER2:'black'}

    def __init__(self):
        self.board = createBoard(ConnectFour.ROWS, ConnectFour.COLS)
        self.num_moves = 0

    def _isValidMove(self, col):
        """ Return True iff the dropping a checker in this col (an int)
        represents a valid move. """
        return self.board[ConnectFour.ROWS-1][col] == ConnectFour.FREE

    def makeMove(self, whichplayer, col):
        """Change the board so that 'whichplayer' occupies the next (vertical)
        spot in the column. Return the integer of the row that the checker is in.
        Parameters:
            whichplayer - an integer representing the player who played the checker
            col - the integer index the player selected.
        """
        

    def showBoard(self):
        csplot.show(self.board, ConnectFour.repToColor)

    def _isDraw(self):
        """ Return True iff the game is a draw because there are no free/empty spots."""
    
    
    def _isWon(self, row, col):
        """ Return True iff the most recent player won."""
        
        whichplayer = self.board[row][col]
        # look around position [row][col]

        # vertically (down)

        # horizontally

        # diagonally
        
        return False

    def _userMakeMove(self):
        """ Allow the user to pick a column. """
        col = csplot.sqinput()
        validMove = self._isValidMove(col)
        while not validMove:
            print("NOT A VALID MOVE.")
            print("PLEASE SELECT AGAIN.")
            print()
            col = csplot.sqinput()
            validMove = self._isValidMove(col)
        return col
        
    def _computerMakeMove(self):
        """Make a move on behalf the computer."""
        # In this case, pick a random column
        col = random.randint(0, ConnectFour.COLS-1)
        validMove = self._isValidMove(col)
        while not validMove:
            col = random.randint(0, ConnectFour.COLS-1)
            validMove = self._isValidMove(col)
        return col 
        
    def play(self):
        won = False
        player = ConnectFour.PLAYER1
        
        # also handle draws besides wins...
        while not won:
            print("Player %d's move" % player)
            if player == ConnectFour.PLAYER1:
                col = self._userMakeMove()
            else: # computer is player 2
                # pause because otherwise move happens to quickly
                # and looks like an error
                sleep(.75)
                col = self._computerMakeMove()
                
            row = self.makeMove(player, col)
            self.showBoard()
            won = self._isWon(row, col)
            
            # alternate players
            player = player % 2 + 1
            
# could create a Checkers or Chess game here...
        
def createBoard(height, width):
    """Returns a board (2D list) with the passed in width and
    height."""
    board = []
    for x in range(height):
        board.append(createOneRow(width))
    return board

            
def createOneRow( n ):
    """ returns a row of n zeros...  You might use
    this as the INNER loop in createBoard """
    row = []
    for col in range(n):
        row.append(0)
    return row

