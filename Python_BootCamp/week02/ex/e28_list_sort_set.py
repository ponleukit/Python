def list_sort_set(List):
    List_unique = []
    for x in List:
        if ( x not in List_unique):
            List_unique.append(x)
    Sort_list_unique = sorted(List_unique)[::-1]
    print(">> {}".format(Sort_list_unique))
    return Sort_list_unique
list_sort_set([4, 2, 19, 50, 49, 48, 1, 2, 3, 4, 5])

