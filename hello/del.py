'''
import os
os.remove("test.txt")
print("Sucessfully... delete")
'''
#Data comparitive deletion
with open("log.txt", "r") as f:
    lines = f.readlines()
ldel = input("Enter the exact line:")
with open("log.txt", "w") as f:
    for line in lines:
        #if line.strip() !='four':
        if line.strip() !=ldel.strip():
            f.write(line)