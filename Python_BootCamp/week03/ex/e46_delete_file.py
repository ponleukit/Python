import os
def delete_file(String):
    if (os.path.exists(String)):
            while True:
                print("Are you sure you want to delete {}? [Y/N]".format(String))
                Answer = input()
                if ( Answer.isdigit()):
                     print("Invalid Option")
                else:
                    if ( Answer == "Y" or Answer == "y"):
                         if(os.path.isdir(String)):
                             os.rmdir(String)
                             return 1
                             break
                         elif(os.path.isfile(String)):
                             os.remove(String)
                             return 1
                             break
                    elif (Answer == "N" or Answer == "n" ):
                        return 0
                        break
                    else:
                        print("Invalid Option")
    else:
        return 0
print(delete_file("44.txt"))
