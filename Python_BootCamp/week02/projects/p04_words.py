import re
def top_words(text):
    empty = []
    Str_List = []
    pre_Result = []
    Result = []
    if ( len(text) == 0 ):
        print(">> {}".format(Str_List))
        return (">> {}".format(Str_List))
    else:
        Lowerstr = text.lower()
        Str_split = Lowerstr.split()
        for x in Str_split:
           Str_List.append(re.sub('^[^a-zA-z]*|[^a-zA-Z]*$','',x))
        Count = {x:Str_List.count(x) for x in Str_List}
        Sort_Count = sorted(Count.items(), key= lambda l:l[1], reverse=True)
        for i in Sort_Count:
            pre_Result.append(i[0])
        if( len(pre_Result) >= 3):
            for i in range(0,3):
                Result.append(pre_Result[i])
            print(Result)
            return Result
        elif( len(pre_Result) == 2):
            for i in range(0,2):
                Result.append(pre_Result[i])
            print(Result)
            return Result
        else:
            for i in pre_Result:
                Result.append(i)
                if ( len(Result[0])== 0 ):
                    print ( empty )
                    return empty
                else:
                    print(Result)
                    return Result
top_words("//can't cant Cant can't")
