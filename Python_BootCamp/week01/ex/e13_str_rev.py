print("Enter a string:")
st = input( ">> " )
st_len = len(st)
if ( st_len != 0 ):
    print( st[::-1] )
else:
    print("The string is empty.")
