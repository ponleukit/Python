def list_sort_str(List):
    New_List = []
    for x in List:
        try:
            if ( x.strip('-').isnumeric()):
                 continue
            else:
                 if( x not in New_List):
                    New_List.append(x)
        except:
            continue
    Sort_list = sorted(New_List, key= lambda l:l[0], reverse= False)
    print(">> {}".format(Sort_list))
    return (">> {}".format(Sort_list))
list_sort_str([ 'abc', 'def', -1, 2, 3, '-123', '888', 'hello'])
