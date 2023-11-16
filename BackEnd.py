import random
from enum import Enum


class Board:
    class FieldTypes(Enum):
        EMPTY = 0
        MINE = 1

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.board = [[None]*n]*m

    def create_mines(self):
        for i in range(self.m):
            for j in range(self.n):
                if random.random() > 0.9:
                    self.board[i][j] = Field(i, j, 1, 0)
                else:
                    self.board[i][j] = Field(i, j, 0, 0)

    def draw_board(self):
        return self.board

class Field:
    def __init__(self, x:int, y:int,  field_type: int, mines_arround: int):
        pass




