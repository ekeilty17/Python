def rule(val, a):
    sum = 0
    for i in a:
        try:
            sum += i
        except:
            return -1

    if (val == 1):
        if (sum == 2 or sum == 3):
            return 1
        else:
            return 0
    else:
        if (sum == 3):
            return 1
        else:
            return 0
