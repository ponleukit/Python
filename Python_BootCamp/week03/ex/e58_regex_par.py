import re
def regex_par(string_word):
    if(len(string_word) == 0):
        return ''
    else:
        Result = re.sub(r'\([^)]*\)','', string_word)
        return Result
regex_par("((not ok)) )ok( )))(not_ok)(((ok")
