import random
class Board:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.board = [[None]*n]*m

    def create_mines(self):
        for i in range(self.n):
            for j in range(self.m):
                if random.random() > 0.9:
                    self.board[i][j] = Field(i, j, 1, 0)
                else:
                    self.board[i][j] = Field(i, j, 1, 0)

    def draw_board(self):
        return self.board

class Field:
    def __init__(self, x:int, y:int,  field_type: int, mines_arround: int):
        pass




