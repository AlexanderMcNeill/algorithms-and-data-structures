__author__ = 'alexmcneill'


import pickle
import os.path
import random
import copy

NAUGHT = 0
CROSS = 1
EMPTY = 2

symbol_list = ["O", "X", "-"]

GRID_SIZE = 3


class GameBoard():

    computer_player = NAUGHT

    def __init__(self, game_grid, player):
        self.game_grid = game_grid
        self.children = []
        self.player = player
        self.next_player = (self.player + 1) % 2
        if not self.check_gameover():
            self.create_child_list()
            self.strategy = self.select_strategy()

    def create_child_list(self):
        # Looping through each slot in the list
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.game_grid[i][j] == EMPTY:
                    self.children.append(self.create_child(i, j))

    def create_child(self, i, j):
        # Creating a new game grid with the move taken
        new_game_grid = copy.deepcopy(self.game_grid)
        new_game_grid[i][j] = self.player

        # Getting the value of the next player
        next_player = self.next_player
        return GameBoard(new_game_grid, next_player)

    def check_gameover(self):
        game_over = False

        for i in range(0, GRID_SIZE):
            if self.game_grid[i][0] == self.game_grid[i][1] and self.game_grid[i][0] == self.game_grid[i][2]:
                if self.game_grid[i][0] != EMPTY:
                    game_over = True
            if self.game_grid[0][i] == self.game_grid[1][i] and self.game_grid[0][i] == self.game_grid[2][i]:
                if self.game_grid[0][i] != EMPTY:
                    game_over = True

        if self.game_grid[0][0] == self.game_grid[1][1] and self.game_grid[0][0] == self.game_grid[2][2]:
            if self.game_grid[0][0] != EMPTY:
                    game_over = True
        if self.game_grid[2][0] == self.game_grid[1][1] and self.game_grid[2][0] == self.game_grid[0][2]:
            if self.game_grid[2][0] != EMPTY:
                    game_over = True

        return game_over

    def select_strategy(self):
        return self.random_move

    def random_move(self):
        return self.children[random.randint(0, len(self.children))]

    def get_matching_child(self, x_pos, y_pos):
        for child in self.children:
            if child.game_grid[x_pos][y_pos] == self.player:
                return child

    def choose_best_move(self):
        return self.strategy()

    def get_grid_string(self):
        output = ""

        # Looping through each slot in the list
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                output += symbol_list[self.game_grid[i][j]]

            output += "\n"

        return output


if __name__ == '__main__':

    game_board = None

    # Getting or creating the game board
    if os.path.isfile("game_board.p"):
        game_board = pickle.load(open("game_board.p", "rb"))
    else:
        starting_game_grid = [[EMPTY for x in range(GRID_SIZE)] for x in range(GRID_SIZE)]
        game_board = GameBoard(starting_game_grid, NAUGHT)
        #  pickle.dump(game_board, open("game_board.p", "wb"))

    finished = False
    # while not finished:
    print game_board.get_grid_string()

    """if game_board.player == NAUGHT:
            game_board = game_board.get_matching_child(0, 0)
        else:
            game_board = game_board.choose_best_move()"""