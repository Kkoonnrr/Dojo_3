from BackEnd import Board

class CmdBoardWriter:
    def __init__(self, n, m) -> None:
        self.back_board = Board(n, m)
        self.back_board.create_mines()
        

        self.board = [["*","*","*"], ["*", "*", "*"]]
    def update_board(self):
        pass

    def get_board_as_string(self) -> str:
        output = ""
        for i in self.board:
            for j in i:
                output += j
            output += "\n"

        return output
    
    def set_flag(self, n, m):
        pass

    def hit_field(self, n, m):
        pass