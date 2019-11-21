import os
def read_file(String):
    check = os.path.exists(String)
    if check:
       Read =  open(String, "r")
       print(Read.read())
       return Read.read()
       Read.close()
    else:
        print("Invalid Filename")
        return ''
read_file("../../week01/week01_ex/e01_welcome.py")
