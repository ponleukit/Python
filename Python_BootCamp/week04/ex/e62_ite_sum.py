def ite_sum(Int_list):
    try:
        Result = 0
        for i in Int_list:
            Result = Result + i
        print(Result)
        return Result
    except:
        return 0
ite_sum([1, 2, 3, 12])
