def sudoku(board):
    count_element = 0
    check_Result1 = 0
    check_Result2 = 0
    sub_board1 = []
    sub_board2 = []
    sub_board3 = []
    sub_board4 = []
    sub_board5 = []
    sub_board6 = []
    sub_board7 = []
    sub_board8 = []
    sub_board9 = []
    for i in range(len(board)):
      for j in range(len(board[i])):
          if ( str(board[i][j]).isdigit()):
              if(0 < int(board[i][j]) < 10):
                 count_element = count_element + 1;
              else:
                  continue
          else:
             continue
    if ( count_element == 81):
            for i in range(0,9):
               for j in range(0,9):
                   for k in range(0, 8):
                     if( board[i][j] != board[i][k+1] and board[j][i] != board[k+1][i]):
                          check_Result1 = check_Result1 + 1
                     else:
                         continue
            for i in range ( 0, 3):
                for j in range ( 0, 3):
                    sub_board1.append(board[i][j])
                    sub_board2.append(board[i][j+3])
                    sub_board3.append(board[i][j+6])
                    sub_board4.append(board[i+3][j])
                    sub_board5.append(board[i+3][j+3])
                    sub_board6.append(board[i+3][j+6])
                    sub_board7.append(board[i+6][j])
                    sub_board8.append(board[i+6][j+3])
                    sub_board9.append(board[i+6][j+6])
            if ( len(set(sub_board1)) == len(set(sub_board2)) ==len(set(sub_board3)) ==len(set(sub_board4)) ==len(set(sub_board5)) ==len(set(sub_board6)) ==len(set(sub_board7)) ==len(set(sub_board8)) ==len(set(sub_board9)) == 9):
                check_Result2 = check_Result2 + 1
            if (check_Result1 ==576 and check_Result2 ==1 ):
                print("Finished")
                return ("Finished")
            else:
                print("Unfinished")
                return ("Unfinished")
    else:
        print("Invalid")
        return ("Invalid")
sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]])

