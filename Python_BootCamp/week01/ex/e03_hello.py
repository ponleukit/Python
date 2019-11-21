try:
 print("Enter a number:")
 num = int(input(">> "))
 for i in range( 0 , num ):
    print("Hello World!")
except ValueError:
    print("Nothing to display.")
