with open("log.txt",'a+') as f:
    f.write("\nend of the line.....\n")
    f.seek(0)
    data=f.read()
    print("Current data:\n",data)