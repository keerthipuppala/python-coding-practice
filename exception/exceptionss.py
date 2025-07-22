try:
    num1= int(input("Enter numerator:"))
    num2= int(input("Enter denominator:"))
    output = num1/num2
    print("Result", output)
except ZeroDivisionError:
    print("Can't divide a number with Zero") 
    
'''
output:
Exception was handled 
KeyboardInterrupt
ValueError

'''