def array_list(List):
      Unique_value_list = []
      if ( len(List) == 0 ):
          print (">> {}".format(Unique_value_list))
          return (">> {}".format(Unique_value_list))
      else:
          for i in List:
              if ( i not in Unique_value_list):
                   Unique_value_list.append(i)
          print(">> {}".format(Unique_value_list))
          return (">> {}".format(Unique_value_list))
array_list([['a','b','c'], ['a'], ['a','b','c'], ['b'], ['a']])
