try:
    print("Enter a number:")
    num1 = int( input(">> ") )
    print("Enter a second number:")
    num2 = int( input(">> ") )
    if num1 < num2:
        print("Result : {} < {}".format( num1 , num2 ))
    elif num1 > num2:
        print("Result : {} < {}".format( num2 , num1 ))
    else:
        print("Result : {} == {}".format( num1 , num2 ))
except ValueError:
   print("")
