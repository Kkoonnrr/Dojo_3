from typing import List
from BackEnd import Board, Field

class CmdBoardWriter:
    def __init__(self, n, m) -> None:
        self.back_board = Board(n, m)
        self.back_board.create_mines()
        self.board_fields:List[List[Field]] = self.back_board.draw_board()


    def update_board(self):
        self.board_fields = self.back_board.draw_board()

    def get_board_as_string(self) -> str:
        output = ""
        for row in self.board_fields:
            print("ROW: ", row[0].x)
            for field in row:
                value = ""
                if(field.hidden):
                    value = "*"
                if(field.flagged == 1):
                    value = "F"
                print(field.x, field.y)
                output+=value

                
            output += "\n"

        return output
    
    def set_flag(self, n, m):
        print("FLAGA: ", n, m)
        self.back_board.set_flag(2, 3)

    def hit_field(self, n, m):
        self.back_board.hit_field(n, m)