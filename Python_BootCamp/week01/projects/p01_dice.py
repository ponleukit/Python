from random import randint
print("Welcome to the dice game!")
result = 0
while True:
    num = input("Enter the number of dice you want to roll:")
    if ( num.isdigit() and int(num) <= 8):
        number = int(num)
        if ( number == 1 ):
            randomnum = randint ( 1 , 6 )
            print("RESULT: {}".format(randomnum))
            break
        else:
            for a in range ( 1 , number + 1 ):
                randomnum = randint ( 1 , 6 )
                print("Dice {} : {}".format(a , randomnum))
                result = result + randomnum
            print("="*10)
            print("RESULT: {}".format(result))
            print("="*10)
            break
    else:
        print("USAGE: The number must be between 1 and 8")
