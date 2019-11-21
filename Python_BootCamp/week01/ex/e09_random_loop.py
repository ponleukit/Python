from random import randint
print("Enter a number:")
num = input( ">> " )
try:
    number_time = int(num)
    for i in range( 0 , number_time ):
     print( randint( 1 , 100 ) )
except ValueError:
    print("")
