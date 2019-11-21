def dict_tuple_key(List):
    if ( len (List) == 0 ):
        print("Your string is empty.")
    else:
        Dict = {str(x):List.count(x) for x in List}
        Dict_to_list = Dict.items()
        List_to_Tuple = tuple(Dict_to_list)
        Sort_Tuple = sorted(List_to_Tuple)
        print(">> {}".format(Sort_Tuple))
        return Sort_Tuple
dict_tuple_key(['c','a','a','a','b','b','b','b','b','b','c','c','c','c'])
