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

    def setValue(self, type):
        self.typ = self.FieldTypes(type)
        return self.typ

    def create_mines(self):
        for i in range(self.m):
            for j in range(self.n):
                if random.random() > 0.9:
                    self.board[i][j] = Field(i, j, self.setValue(1), 0, 1, 0)
                else:
                    self.board[i][j] = Field(i, j, self.setValue(0), 0, 1, 0)

    def draw_board(self):
        return self.board

    def get_field(self, x, y):
        return self.board[x][y]

    def set_flag(self, n, m):
        self.board[n][m].flagged = 1

    def hit_field(self, n, m):
        self.board[n][m].hidden = 0


class Field:
    def __init__(self, x:int, y:int,  field_type, mines_around: int, hidden: int, flagged: int):
        self.x = x
        self.y = y
        self.field_type = field_type
        self.mines_around = mines_around
        self.hidden = hidden
        self.flagged = flagged





