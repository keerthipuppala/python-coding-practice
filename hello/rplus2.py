with open("fiele1.txt", 'w+') as f:
    f.write("Hello Student!!")
    f.seek(0)
    data = f.read()
    print("Previous:",data)
    new_data = data.replace("Student!!", "Sataya_Sri_Keerthi")
    f.seek(0)
    f.write(new_data)
    f.truncate()
with open("fiele1.txt", 'r') as f:
    data=f.read()
    print("Latest:", data)