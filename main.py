from CMDboard import CmdBoardWriter

writer = CmdBoardWriter(9, 10)

while(True):
    writer.update_board()
    print(writer.get_board_as_string())

    in_f = input('Do you want to set flag (1) or hit (2) \n')
    in_values = input('which field width, height \n')
    m_n = [int(i) for i in in_values.split(", ")]
    if(in_f == '1'):
        writer.set_flag(m_n[0], m_n[1])
    elif(in_f == '2'):
        writer.hit_field(m_n[0], m_n[1])