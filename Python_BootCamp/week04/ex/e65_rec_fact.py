def rec_fact(Int_num):
    try:
        if Int_num == 0:
            return 1
        else:
            return Int_num * rec_fact( Int_num - 1)
    except:
        return 0
rec_fact(7)
