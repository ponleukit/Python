Start_Program = True
import array as arr

"""Menu"""
print("Menu: \n a: Create Stack \n b: Push \n c: Pop \n d: Display \n e: check palindrom \n f: Exit" )

GrobalStack = 0
class Stack:
    def __init__(self):
        self.sizeStackArray = int(input("Enter the size of ArrayStack: "))
        self._data = list()
    def __Push__(self, data):
        if(len(self._data) >= self.sizeStackArray):
            print("Stack overFlow")
        else:
            self._data.append(data)
            print(data + " has been added to the stack. ")
    def __Pop__(self):
        if(len(self._data) > 0):
            print(self._data[len(self._data) - 1] + " has been remove from stack")
            self._data.pop()
        else:
            print("Stack underFlow")
    def __peek__(self):
        if(len(self._data) == 0):
            print("Stack is empty")
        else:
            print(self._data)
    def check_Palindrome(self):
        reversed_list = list()
        for i in range(len(self._data)):
            reversed_list.append(self._data[len(self._data) - 1 - i])
        if reversed_list == self._data:
            print("It is palidrom")
        else:
            print("It isn't palidrom")

"""Check Stack weather has created or not"""
def check_stack(choosen_menu):
    if(GrobalStack == 0):
        print("Stack hasn't created")
    else:
        if (choosen_menu == "b"):
            data = input("Enter the value: ")
            GrobalStack.__Push__(data)
        elif (choosen_menu == "c"):
            GrobalStack.__Pop__()
        elif (choosen_menu == "d"):
            GrobalStack.__peek__()
        elif (choosen_menu == "e"):
            GrobalStack.check_Palindrome()

while Start_Program:
    """Choose Menu"""
    menu = input("Choose Menu: ")
    if (menu == "a"):
        GrobalStack = Stack()
    elif (menu == "b"):
        check_stack(menu)
    elif (menu == "c"):
        check_stack(menu)
    elif (menu == "d"):
        check_stack(menu)
    elif (menu == "e"):
        check_stack(menu)
    elif (menu == "f"):
        Start_Program = False
        break
