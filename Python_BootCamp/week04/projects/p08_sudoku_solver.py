def Check_position_safe(Sudoku_list1, row, column, number):
    for i in range(9):
        if (Sudoku_list1[row][i] == number):
            return False
        if (Sudoku_list1[i][column] == number):
            return False
        for j in range(3):
            for k in range(3):
                if (Sudoku_list1[j + (row - row%3)][k + (column - column%3)] == number):
                    return False
    return True
def Check_emptyposition(Sudoku_list, makerl):
    for i in range(9):
        for j in range(9):
            if (Sudoku_list[i][j] == 0):
                makerl[0] = i
                makerl[1] = j
                return True
    return False

def Try_to_solve(Sudoku_list1, makerl ):

    if ( not Check_emptyposition(Sudoku_list1, makerl)):
        return True
    row = makerl[0]
    column = makerl[1]

    for number in range(1,10):
        if ( Check_position_safe(Sudoku_list1, row, column, number) ):
            Sudoku_list1[row][column] = number
            if(Try_to_solve(Sudoku_list1, makerl)):
                return True
            Sudoku_list1[row][column] = 0
    return False
def sudoku_solver(sudoku_list):
    if (Try_to_solve(sudoku_list, [0,0])):
        List = []
        for i in sudoku_list:
            list1 = []
            for j in i:
                list1.append(j)
            List.append(list1)
        for i in List:
            print(i)
sudoku_solver([ [5, 3, 4, 6, 7, 0, 9, 0, 2],
                [6, 7, 2, 0, 9, 5, 3, 0, 0],
                [0, 9, 0, 3, 0, 2, 5, 6, 7],
                [0, 5, 9, 7, 6, 0, 0, 2, 3],
                [0, 2, 6, 0, 5, 3, 7, 9, 0],
                [7, 0, 3, 9, 2, 0, 0, 5, 6],
                [9, 6, 0, 5, 3, 7, 2, 0, 0],
                [2, 0, 7, 0, 0, 9, 6, 3, 5],
                [3, 0, 5, 2, 0, 6, 0, 7, 9]])
