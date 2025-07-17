'''
file = open("test.txt","w")
file.write("congratulations....")
file.close()

'''
'''
file = open("test.txt","a")
file.write("but us are not this session")
file.close()

'''
with open("sample_bnary.bin","wb") as file:
    data = b'\x48\x65\x6c\x6c\x6f'
    file.write(data)
