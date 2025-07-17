filename = input("enter your file name: ")
with open(filename, 'r') as file:
    text = file.read()
    letter = input("Enter char")
    c=0
    for char in text:
        if char == letter:
            c+=1
print(letter, "append" , c , "time in the file")