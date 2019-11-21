import re
def regex_word(num, string_word):
    if ( num <= 0 ):
        return ""
    else:
        Result  = re.sub(r'\W*\b\w{1,n}\b'.replace('n',str(num)),'',string_word)
        return Result
regex_word (2, "Is it a cat or a dog?" )
