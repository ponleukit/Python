start_program = True
import array
G_array = 0

"""Menu"""

print("Menu: \n a: create the array \n b: display the array \n c: inserting the element \n d: deleting the element in the specific position \n e: Exit")

"""Starting Program"""

while start_program:
    menu = input("Enter the option: ")
    if(menu == "a"):
       lengOfArray = int(input("Input the length of Array: "))
       G_array = []
       for i in range(lengOfArray):
           G_array.append(None)
       print("Array has been created")
    elif(menu == "b"):
        if G_array == 0:
            print("Array hasn't created")
        else:
            display()
    elif(menu == "c"):
        if G_array == 0:
            print("Array hasn't created")
        else:
            print("please enter the value and its position")
            value = int(input("value: "))
            position = int(input("position: "))
            inserting(value, position - 1)
    elif(menu == "d"):
        if G_array == 0:
            print("Array hasn't created")
        else:
            print("please enter the position of element: ")
            position = int(input())
            deleting(position)
    elif(menu == "e"):
        start_program = False
    """function"""
    def display():
        if (len(G_array) == 0):
            print("Array is Empty")
        else:
            print(G_array)
    def inserting(value, position):

        G_array[position] = value
        print(str(value) + " has been inserting in position: " + str(position) )
    def deleting(position):
        G_array[position - 1] = None
