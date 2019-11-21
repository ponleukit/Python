def fun_tuple(string , num):
    Recieve_list = list()
    Recieve_list.append(string)
    Recieve_list.append(num)
    Tuple_the_string = tuple(Recieve_list)
    print(">> {}".format(Tuple_the_string))
    return Tuple_the_string
fun_tuple( 'abc' , 123 )
