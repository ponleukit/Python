print("Enter a title:")
title = input( ">> " )
title_len = len(title)
if ( title_len != 0 ):
    print("<h1>"+ title + "</h1>")
else:
    print("Nothing to display.")
