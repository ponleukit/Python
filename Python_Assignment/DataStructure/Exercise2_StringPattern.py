def _replace( str, pat, rep):
     if pat in str:
         list = []
         for i in range(str.count(pat)):
             x = str.find(pat)
             list.append(str[:x])
             list.append(rep)
             str = str[x + len(pat):]
         x = (x+len(str))*str.count(pat)
         list.append(str[x-2:])
         return(''.join(list))
     else:
       return str

Str = input("Enter the main string: ")
Pat = input("Enter the string pattern: ")
Rep = input("Enter the replace string: ")

result = _replace(Str, Pat, Rep)
print(result)
