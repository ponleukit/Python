import os
def write_file(filename,content):
    check = os.path.exists(filename)
    if check:
        while True:
            print("Are you sure you want to replace {}? [Y/N]".format(filename))
            Answer = input()
            if ( Answer.isdigit()):
                print("Invalid Option")
            else:
                if ( Answer == "Y" or Answer == "y"):
                    f = open(filename, "w+")
                    f.write(content)
                    f.close()
                    return 1
                    break
                elif ( Answer == "N" or Answer == "n"):
                    return 0
                    break
                else:
                    print("Invalid Option")
    else:
        f = open(filename,"w+")
        f.write(content)
        f.close()
        return 1
write_file("44.txt", "I like you ponleu")
