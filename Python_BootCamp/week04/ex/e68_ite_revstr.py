def ite_revstr(String):
      if isinstance(String, str):
        Result = ''
        for i in range(0, len(String)):
            Result = Result + String[len(String) - 1 - i]
        return Result
      else:
          return 0
ite_revstr(-7)
