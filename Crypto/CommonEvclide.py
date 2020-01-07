import Crypto.evclide as evclide

def CommonEvclide(a, b):

    arg1 = [a, 1, 0]
    arg2 = [b, 0, 1]
    turn = False
    if a < b:
        turn = True
        arg1 = [b, 1, 0]
        arg2 = [a, 0, 1]
    
    while arg2[0] != 0:
        arg = arg1[0] // arg2[0]
        newarg =[arg1[0] % arg2[0], arg1[1] - arg * arg2[1], arg1[2] - arg * arg2[2]]
        arg1 = arg2
        arg2 = newarg

    if turn:
        return [evclide.Evclide(a, b), arg1[2], arg1[1]]
    else:
        return [evclide.Evclide(a, b), arg1[1], arg1[2]]
    
if __name__ == "__main__":
    print(CommonEvclide(19, 28))

