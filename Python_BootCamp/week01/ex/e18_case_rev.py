print("Enter a string:")
st = input( ">> " )
st_len = len(st)
# newst uses to display the result
newst = ""
if ( st_len != 0 ):
    for a in range( 0 , len(st) ):
        if ( st[a].islower() ):
            newst += st[a].upper()
        else:
            newst += st[a].lower()
    print(newst)
else:
    print("Empty")
