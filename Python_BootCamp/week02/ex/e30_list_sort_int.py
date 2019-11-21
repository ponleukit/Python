def list_sort_int(List):
    List_int = []
    for x in List:
        try:
            if ( int(x) not in List_int ):
                List_int.append(int(x))
            else:
                continue
        except:
            continue
    Result = sorted(List_int)
    print(">> {}".format(Result))
    return Result
list_sort_int(['1','3','5','1','-4','abc', '22', 23, 'abc123'])
