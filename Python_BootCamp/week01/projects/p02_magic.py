#The requirment of this program doesn't specefic what we have to do when the user input the string in guessing number
#So when the user input the string in guessing parth, the program will waiting untill the user input integer
from random import randint
Game_running = True
print("Hello, what is your name?")
name = input( ">> " )
def Loop_Game():
    #use count_time to consider if the player win at the first or not
    while Game_running:
        random = randint ( 1 , 88 )
        count_time = 0
        print("Well {}, try to guess the number I have in mind!".format(name))
        while True:
            num = input(">> ")
            if ( num.isdigit() ):
                number = int( num )
                if ( number in range ( 1 , 88 ) ):
                    count_time = count_time + 1
                    if ( number == random ):
                        if ( count_time == 1 ):
                            print("You won in 1 turn only, that's amazing!")
                        else:
                            print("It took you %d turns to guess my number which was %d!" %( count_time , random))
                        while True:
                            print("Do you want to play again? [Y/N]")
                            ans = input()
                            if ( ans == "N"):
                                print("Ok, bye {}! See you later!".format(name))
                                break
                            elif ( ans == "Y"):
                                 Loop_Game()
                                 break
                            else:
                                print("Sorry, I did not understand. Let me repeat:")

                        break
                    else:
                        if ( number > random ):
                            print("Too high, try again!")
                        else:
                            print("Too low, try again!")
                else:
                     print("Invalid number, USAGE: 1-88, try again!")
        break
Loop_Game()
