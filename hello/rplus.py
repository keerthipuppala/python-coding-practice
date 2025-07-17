with open("fiele1.txt", 'w') as f:
    f.write("keerthi Puppala")
with open("fiele1.txt", 'r+') as f:
    data = f.read()
    print("Previous:",data)
    new_data = data.replace("keerthi", "Sataya_Sri_Keerthi")
    f.seek(0)
    f.write(new_data)
    f.truncate()
with open("fiele1.txt", 'r') as f:
    data=f.read()
    print("Latest:", data)