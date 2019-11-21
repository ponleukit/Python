import os
import datetime
import os.path
class Filelib:
    #current_path
    def current_path():
      print(os.getcwd())
      return os.getcwd()
    #current_file
    def current_files():
          List_file = []
          List_dir = []
          Result = []
          for file in os.scandir('.'):
            if file.is_file():
              List_file.append(tuple([file.name, "File"]))
            elif os.path.isdir(os.getcwd()):
               List_dir.append(tuple([file.name, "Folder"]))
          List_file = sorted(List_file, key= lambda L:L[0],reverse=False)
          List_dir  = sorted(List_dir, key = lambda L:L[0], reverse=False)
          Result = (List_file + List_dir)
          print(Result)
          return Result
    #read_file
    def read_file(filename):
        check = os.path.exists(filename)
        if check:
           Read =  open(filename, "r")
           print(Read.read())
           return Read.read()
           Read.close()
        else:
            print("Invalid Filename")
            return ''
    #write_file
    def write_file(filename, content):
        if os.path.exists(filename):
            f = open(filename, 'w+')
            f.write(content)
            f.close()
            return 1
        else:
            f = open(filename,'w+')
            f.write(content)
            f.close()
            return 1
    #delete_file
    def delete_file(filename):
        if (os.path.exists(filename)):
             if(os.path.isdir(filename)):
                 os.rmdir(filename)
                 return 1
             elif(os.path.isfile(filename)):
                 os.remove(filename)
                 return 1
        else:
            return 0
    #create_folder
    def create_folder(folder_list):
         count_folder = 0
         if ( len(folder_list) == 0):
             return 0
         else:
            check = []
            for i in range(0, len(folder_list)):
                check.append(os.path.exists(folder_list[i]))
            for i in range(0, len(check)):
                if ( check[i] == False):
                    os.mkdir(folder_list[i])
                    count_folder = count_folder + 1
                else:
                    os.rmdir(folder_list[i])
                    os.mkdir(folder_list[i])
                    count_folder = count_folder + 1
         print(count_folder)
         return count_folder
