import  os
def create_folder(List_String):
     count_folder = 0
     if ( len(List_String) == 0):
         return 0
     else:
        check = []
        for i in range(0, len(List_String)):
            check.append(os.path.exists(List_String[i]))
        for i in range(0, len(check)):
            if ( check[i] == False):
                os.mkdir(List_String[i])
                count_folder = count_folder + 1
            else:
                while True:
                    print("Are you sure you want to replace {}? [Y/N]".format(List_String[i]))
                    Answer = input()
                    if ( Answer.isdigit()):
                        print("Invalid Option")
                    else:
                        if ( Answer == "Y" or Answer == "y"):
                            os.rmdir(List_String[i])
                            os.mkdir(List_String[i])
                            count_folder = count_folder + 1
                            break
                        elif ( Answer == "N" or Answer == "n"):
                            break
                        else:
                            print("Invalid Option")
     print(count_folder)
     return count_folder
create_folder(["Hello", "world","goodbye","orld","Moon"])

