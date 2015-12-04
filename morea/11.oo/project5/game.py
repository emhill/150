""" Plays ConnectFour game. """

import csplot
from connectfour import *

def main():

    game = ConnectFour()
    game.showBoard()
    game.play()
    

main()


