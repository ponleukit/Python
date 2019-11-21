print("Enter your encrypted message:")
st = input(">> ")
message = ""
if ( len(st) != 0):
    if ( st.isnumeric() ):
       print("Nothing to decode.")
    else:
       for a in range( 0 , len(st) ):
           if ( 64 < ord( st[a] ) < 78 or 96 < ord( st[a] ) < 110 ):
             message += chr( ord( st[a] )+13)
           elif ( 77 < ord ( st[a] ) < 91 or 109 < ord ( st[a] ) < 123 ):
             message += chr( ord( st[a] ) - 13 )
           else:
               message += st[a]
    print(message)
else:
    print("Nothing to decode.")
