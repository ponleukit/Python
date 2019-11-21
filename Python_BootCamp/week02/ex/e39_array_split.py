def array_split(List):
    Split_array = []
    if ( len(List) == 0 ):
        Split_array
        return Split_array
    else:
        for x in List:
            Split_array.append(list(x))
        print(">> {}".format(Split_array))
        return Split_array
array_split(['world', 'wide', 'web'])

