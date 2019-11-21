from datetime import datetime
def timestamp_to_str(Timestamp):
     try:
       Obj_timestamp = datetime.fromtimestamp(Timestamp)
       Result = Obj_timestamp.strftime("%Y-%m-%d %H:%M:%S")
       print(">> {}".format(Result))
       return Result
     except:
         if(Timestamp.isnumeric()):
             Timestamp_to_int = int(Timestamp)
             Result = datetime.fromtimestamp(Timestamp_to_int)
             print(">> {}".format(Result))
             return Result
         else:
             print("Your timestamp is not valid.")
             return 0
timestamp_to_str(1623646780)
