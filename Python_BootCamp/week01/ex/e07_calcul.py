total = 0
Code_running = True
while Code_running:
    print("Enter a number:")
    num = input( ">> " )
    try:
        number = int(num)
        total = total + number
        print("TOTAL: {}".format(total))
    except ValueError:
        if num == "exit":
            break
        else:
            print("TOTAL: {}".format(total))
