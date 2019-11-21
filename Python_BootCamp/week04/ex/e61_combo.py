from itertools import combinations
def display_combo():
    Check = combinations(range(0,10),3)
    RESULT = ''
    for i in Check:
        Nstr = ""
        for a in i:
            Nstr += str(a)
        RESULT = RESULT + ', '+  Nstr
    print(RESULT[1:][1:])
display_combo()
