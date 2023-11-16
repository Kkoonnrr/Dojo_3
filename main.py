from CMDboard import CmdBoardWriter

writer = CmdBoardWriter(9, 10)

while(True):
    writer.update_board()
    print(writer.get_board_as_string())
    in_f = input('Do you want to set flag (1) or hit (2) \n')
    in_values = input('which field width, height \n')

    while True:
        try:
            assert(in_f in ["1", "2"])
            m_n = [int(i) for i in in_values.split(", ")]
            assert(len(m_n) == 2)
        except Exception as e:
            print("Try again")
            in_f = input('Do you want to set flag (1) or hit (2) \n')
            in_values = input('which field width, height \n')
            continue
        else:
            #the rest of the code
            break

    if(in_f == '1'):
        writer.set_flag(m_n[0], m_n[1])
    elif(in_f == '2'):
        writer.hit_field(m_n[0], m_n[1])