#this count_GEN is use to display the paragraph when count_GEN == 1 and break the loop when count_GEN == 2
count_GEN = 0
#stlist is the list uses to store the string that we've had input.
stlist = []
while True:
    print("Enter a string:")
    st = input( ">> " )
    if ( st != "GEN" ):
        stlist.append(st)
    else:
        count_GEN = count_GEN + 1
        if ( count_GEN == 1 ):
           for a in range( 0 , len(stlist)  ):
               print( "<p>" + stlist[a] + "</p>" )
        elif( count_GEN == 2):
            print("Nothing to display.")
            break
        else:
            break
