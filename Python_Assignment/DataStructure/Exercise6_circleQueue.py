"""Menu"""
print("Menu: \n a: Inserting element into circular Queue \n b: Deleting element from circular Queue \n c: Display circular Queue \n d: Exit")

"""Starting program"""

Start_program = True

"""Define the leng of Circular Queue"""

QueueLength = int(input("Enter the leng of Circular Queue: "))

check_overFlow_and_underFlow = []

class Node:33
      def __init__(self):
          self.data = None
          self.link = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


def enQueue(q, value):
    temp = Node()
    temp.data = value
    check_overFlow_and_underFlow.append(value)
    if(len(check_overFlow_and_underFlow) > QueueLength):
        print("Queue overFlow")
    else:
        if q.front == None:
            q.front = temp
        else:
            q.rear.link = temp
        q.rear = temp
        q.rear.link = q.front
        print(value + " has been add to Queue")
def deQueue(q):
    value = None
    if(q.front == None):
        print("Queue underFlow")
        return -1
    else:
        if(len(check_overFlow_and_underFlow) == 1):
            q.front = None
            q.rear  = None
        else:
            temp = q.front
            value = temp.data
            q.front = q.front.link
            q.rear.link= q.front

    print( check_overFlow_and_underFlow[len(check_overFlow_and_underFlow) - 1] + " has been removed")
    check_overFlow_and_underFlow.pop()

    return value
def Display(q):

    temp = q.front

    while (temp.link != q.front):
        print(temp.data, end = " ")
        temp = temp.link
    print(temp.data)

if __name__ == "__main__":

    q = Queue()
    q.front = q.rear = None

    while Start_program:
        menu = input("Choose menu: ")
        if (menu == "a"):
            data = input("Enter the value: ")
            enQueue(q,data)
        elif (menu == "b"):
            deQueue(q)
        elif (menu == "c"):
            Display(q)
        elif (menu == "d"):
            Start_program = False
