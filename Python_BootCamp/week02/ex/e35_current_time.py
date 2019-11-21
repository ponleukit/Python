from datetime import datetime
def current_time():
    current = datetime.now()
    Current_time = current.strftime("%H:%M:%S")
    print (">> {}".format(Current_time))
    return Current_time
current_time()

