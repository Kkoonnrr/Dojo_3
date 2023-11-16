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
        for i in self.board_fields:
            for field in i:
                value = ""
                if(field.hidden):
                    value = "*"
                elif(field.flagged):
                    value = "F"
                output+=value
            output += "\n"

        return output
    
    def set_flag(self, n, m):
        pass

    def hit_field(self, n, m):
        pass