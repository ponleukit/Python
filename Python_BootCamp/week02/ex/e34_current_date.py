from datetime import datetime
def current_date():
    now = datetime.now()
    current = now.strftime("%Y-%m-%d")
    print (">> {}".format(current))
    return current
current_date()
