print("Enter a string:")
st = input( ">> " )
st_len = len(st)
if ( st_len != 0 ):
    print( st[ len(st) - 1 ] )
else:
    print("Empty")
