def ite_power(num, power):
    try:
        if str(power).isdigit():
            if power == 0:
                if isinstance(num , str):
                    return 0
                else:
                    return 1
            else:
                Result = 1
                for i in range(0, power):
                    Result = Result * num
                return Result
        else:
            if int(power) < 0:
                Result = 1
                power = power * (-1)
                for j in range(0, power):
                    Result = Result * (1/num)
                return Result
            else:
                return 0
    except:
        return 0
ite_power(3, 0)
