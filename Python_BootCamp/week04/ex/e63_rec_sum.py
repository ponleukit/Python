def rec_sum(Int_list):
    try:
        if not Int_list:
            return 0
        else:
            return Int_list[0] + rec_sum(Int_list[1:])
    except:
        return 0
rec_sum([1, 2, 3, 4, 5, 6, 7, 8, 9])
