import os
import os.path
def current_files():
  List_file = []
  List_dir = []
  for file in os.scandir('.'):
    if file.is_file():
      List_file.append(tuple([file.name, "File"]))
    elif os.path.isdir(os.getcwd()):
       List_dir.append(tuple([file.name, "Folder"]))
  List_file = sorted(List_file, key = lambda L:L[0], reverse = False)
  List_dir  = sorted(List_dir, key  = lambda L:L[0], reverse = False)
  Result = (List_file + List_dir)
  print(Result)
  return Result
current_files()
