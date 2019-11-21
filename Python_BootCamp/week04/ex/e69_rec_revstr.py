def rec_revstr(String):
    if isinstance(String, str):
        Newstring = str(String)
        if Newstring == '':
            return Newstring
        else:
            return rec_revstr(Newstring[1:]) + Newstring[0]
    else:
        return 0
rec_revstr("Hello world")
