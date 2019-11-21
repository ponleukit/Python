def ite_fact(Int_agrs):
    try:
        if Int_agrs < 0:
            return 0
        else:
           Result = 1
           for i in range(1, Int_agrs + 1):
               Result = Result * i
           return Result
    except:
        return 0
ite_fact(7)
