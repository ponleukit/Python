import os
from datetime import datetime
def log_file(filename):
     Message_List = []
     Message_Time = []
     Write_message_into_list = []
     while True:
         message = input("$: ")
         if ( message == "EXIT"):
                 break
         else:
            message_to_string = str(message)
            Message_List.append(message_to_string)
            Message_Time.append(datetime.now().strftime('[%d/%m/%Y %H:%M:%S] '))
     for i in range(0, len(Message_List)):
         Write_message_into_list.append(Message_Time[i] + Message_List[i])
     with open(filename, 'a') as filecontent:
         for item in Write_message_into_list:
             filecontent.write("{}\n".format(item))
log_file("CHANNA_crush.txt")
