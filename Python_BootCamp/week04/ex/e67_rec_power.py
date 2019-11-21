def ite_power(num, power):
    try:
        if str(power).isdigit():
            if power == 0 :
               if isinstance(num, str):
                   return 0
               else:
                   return 1
            else:
                return num * ite_power(num, power -1)
        else:
            if int(power) < 0:
                power = power * (-1)
                return 1/(num * ite_power(num, power -1))
            else:
                return 0
    except:
        return 0
ite_power(-12, 4)
