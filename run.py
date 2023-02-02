
#Game rules
#X for placing ship and hitting a battleship
# ' ' for avaulable space
# '-' for missed attempt

"""
import rand.it
"""
from random import randint


#Boards for both player on comp
HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]


let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


"""
main functions
"""


def print_board(board):
    print('   A B C D E F G H')
    print('   ---------------')
    row_number = 1
    """
    This iterates through each row in the board and joins the pipes
    """
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = "X"

def get_ship_location():
    pass


def count_hit_ships():
    pass


"""
#game process
create_ships()
turns = 10
while turns > 0:
"""

