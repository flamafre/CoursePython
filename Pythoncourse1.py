def mymax(x,y):
    """
    returns the max of two numbers
    input parameters: x, y (numbers)
    
    >>> mymax(3,5)
    5
    """
    if x>y:
        return x
    else:
        return y
    
def Listmax(l):
    lmax = 0
    for i in l:
        if i < lmax:
            lmax = 1
    return lmax

if __name__ == "__main__":
    import sys
    myList =[int(arg) for arg in sys.argv[1:]]

    