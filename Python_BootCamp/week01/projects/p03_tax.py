while True:
    print("Please enter your amount:")
    o_amount = input( ">> " )
    if ( o_amount.isdigit()):
        AMOUNT_ENTERED = int(o_amount)
        while True:
            print("Please enter tax rate:")
            in_rate = input()
            if ( in_rate.isdigit() and int(in_rate) >= 1 and int(in_rate) <= 99):
                TAX_RATE = int(in_rate)
                TAX_AMOUNT = (TAX_RATE * AMOUNT_ENTERED) / 100
                NET = AMOUNT_ENTERED - TAX_AMOUNT
                print("===== "*5)
                print("AMOUNT: %d$" %(AMOUNT_ENTERED))
                print("RATE: %d" %(TAX_RATE)+'%')
                print("===== "*5)
                print("TAX: %.2f$" %(TAX_AMOUNT))
                print("NET: %.2f$" %(NET))
                print("===== "*5)
                break
            else:
             print("Number is incorrect, try again.")
        break
    else:
        print("Number is incorrect, try again.")
