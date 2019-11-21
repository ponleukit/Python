Code_running = True
while Code_running:
    print("Enter a number:")
    num = input( ">> " )
    try:
        number = int(num)
        if number % 2 == 1:
            print("{} is ODD".format(number))
        else:
            print("{} is EVEN".format(number))
    except:
        st = str(num)
        if st == "exit" or num == "EXIT":
            break
        else:
            print("{} is not a valid number.".format(st))
