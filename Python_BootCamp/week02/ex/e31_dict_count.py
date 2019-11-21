from operator import itemgetter
def dict_count(List):
     Dict = {str(x):List.count(x) for x in List}
     Dict_to_list = Dict.items()
     Sort_list = sorted(Dict_to_list, key=lambda x: (x[0],x[1]), reverse=False)
     List_to_Dict = dict(Sort_list)
     print(">> {}".format(List_to_Dict))
     return List_to_Dict
dict_count([ 'c','a','a','a','b','b','b','b','b','b','c','c','c','c'])
