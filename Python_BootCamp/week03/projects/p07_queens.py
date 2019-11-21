from itertools import permutations
from itertools import combinations
def queens():
    #final all possible solution
    All_possible_list = []
    counted = 0
    for i in permutations(range(1,9)):
        All_possible_list.append(list(zip(range(1,9),i)))
    for Real_solutions in All_possible_list:
        Check_conditions = []
        #check the diangal
        for Check1, Check2 in combinations(Real_solutions, 2):
            if ( (Check2[1] - Check1[1])/(Check2[0] - Check1[0]) == 1 or (Check2[1] - Check1[1])/ (Check2[0] - Check1[0]) == -1):
                Check_conditions.append(1)
            else:
                Check_conditions.append(0)
        if 1 not in Check_conditions:
            print(Real_solutions)
            counted = counted + 1
    print(counted)
    return counted
queens()
