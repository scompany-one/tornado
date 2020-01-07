

def Evclide(a, b):
    
    arg1 = a if a >= b else a
    arg2 = b if a >= b else b

    while arg2 > 0:
        r = arg1 % arg2
        arg1 = arg2
        arg2 = r

    return arg1