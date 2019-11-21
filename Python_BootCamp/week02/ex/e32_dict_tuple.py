def dict_tuple(List):
    if ( len(List) == 0 ):
        print("Your string is empty.")
        return ("Your string is empty.")
    else:
        Dict = {x:List.count(x) for x in List}
        Sort_list = sorted(Dict.items(), key = lambda x: (x[1], -ord(x[0])), reverse= True)
        print (">> {}".format(Sort_list))
        return Sort_list
dict_tuple([ 'c','a','a','a','b','c','c','b','b','b','b'])
