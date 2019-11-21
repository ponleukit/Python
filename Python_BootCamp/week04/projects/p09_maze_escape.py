class Maze:
    def check(self,maze):
        row = 0
        check_m = 0
        List1= []
        for i in maze:
            row = row + 1
            column = 0
            for j in i:
                column = column + 1
                if ( j == "#" or j == " " or j == "m"):
                    List1.append(j)
                    if(j ==  "m" ):
                        check_m = check_m + 1

        if ( len(List1) == row*column and check_m == 1):
            return True
        else:
             return  False

Maze().check([
                ['#', '#', '#', ' ', '#'],
                ['#', ' ', '#', '#', '#'],
                ['#', ' ', ' ', 'm', ' '],
                ['#', '#', '#', '#', '#']])
