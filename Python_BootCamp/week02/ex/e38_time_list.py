from datetime import datetime
def time_list(n):
    current = datetime.now()
    Datetime = current.strftime("%H:%M:%S")
    List_datetime = []
    try:
        for i in range (0, n):
           List_datetime.append(Datetime)
        print(">> {}".format(List_datetime))
        return List_datetime
    except:
        print(">> {}".format(List_datetime))
        return List_datetime
time_list(5)
