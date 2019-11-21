def list_set(List):
    unique_list = []
    for x in List:
        if ( x not in unique_list ):
            unique_list.append(x)
    print(">> {}".format(unique_list))
    return unique_list
list_set(['456', '123', '789', '123', 'abc', 'abc', 'def'])
