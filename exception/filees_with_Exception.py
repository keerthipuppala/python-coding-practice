try:
    '''
    filename = input("Enter the file name:")
    file = open(filename, 'r')
    number = int(file.readline())
    print("Number from file", number)
    '''
    file = open('file1.txt', 'a')
    num  = int(input("Enter the number:"))
    num2 = int(input("enter the number to divide:"))
    print(num/num2)
    
except FileNotFoundError:
    print("\nFile does not Exist...")
except KeyboardInterrupt:
    file.write("\nKey board Error....")
except ValueError:
    file.write("\nvalue error...")
except ZeroDivisionError:
    file.write("\nZeroDivisionError...")
    
file.close()