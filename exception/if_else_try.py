import math
'''
try:
    num = int(input("Enter the number"))
    if num<0:
        raise ValueError("Nagative number....")
except ValueError:
    print("Enter the positive number onlyy.....")
else:
    print("SquareRoot", round(math.sqrt(num),4))
    '''
try:
    num = int(input("Enter the number:"))
    print(num)
    raise ValueError
except:
    print("Exception raised intentionally even no use....")