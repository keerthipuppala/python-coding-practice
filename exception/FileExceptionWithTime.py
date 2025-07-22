import datetime
try:
    x= int(input("enter numerator:"))
    y = int(input("Enter denomiator"))
    print("result",x/y)
except (ZeroDivisionError) as e :
    ct = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    txt = f"[{ct}] Error: {str(e)}\n"
    with open("file1.txt", "a") as f:
        f.write(txt)
except (ValueError) as e :
    ct = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    txt = f"[{ct}] Error: {str(e)}\n"
    with open("file1.txt", "a") as f:
        f.write(txt)