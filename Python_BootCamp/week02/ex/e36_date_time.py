from datetime import datetime
def date_time():
    now = datetime.now()
    Date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(">> {}".format(Date_time))
    return Date_time
date_time()
