'''
try:
    filename = input("Enter the file name:")
    file = open(filename, 'r')
    number = int(file.readline())
    print("Number from file", number)
    file.close()
except FileNotFoundError:
    print("File does not Exist...")
except ValueError:
    print("File does not have integer....")
except:
    print("Unkow Error..")
    '''   
try:
    num  = int(input("Enter the number"))
    print(num*3)
except (KeyboardInterrupt,ValueError,TypeError):
    print("Please check before executing...")
print("Program Terminated...")