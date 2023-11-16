class CmdBoardWriter:
    def __init__(self, m, n) -> None:
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
    
    def set_flag(self, m, n):
        pass

    def hit_field(self, m, n):
        pass