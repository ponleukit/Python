import re
def regex_alpha_k(String):
    Compare = re.sub('[^a-kA-K0-5]','',String)
    if(len(String) == 0):
       return False
    else:
        if ( Compare == String):
            return True
        else:
            return False
regex_alpha_k ( "aBc123k5" )
