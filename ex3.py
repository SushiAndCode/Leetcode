
def reverse( x):
    """
    :type x: int
    :rtype: int
    """
    if not x:
        return 0
    
    minus = False
    if x < 0:
        minus = True
        x = x[1:]
        reverse = x[::-1] 
    else:
        reverse = str(x)[::-1]

    while reverse and reverse[0] == '0':
        reverse = reverse[1:]
    
    if minus:
        reverse='-'+reverse
    
    if int(reverse) > pow(2,31) or int(reverse) < -pow(2,31):
        return 0

    return int(reverse)

reverse(-1563847412)