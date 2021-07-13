import struct, os

def read_data():
    os.chdir('/home/josh/Code/ICEYE TASK/ICEYE Task')
    with open('telemetry.bin','rb') as file:
        data = file.read()
    return data

data = read_data()
[print(data[i]) for i in range(len(data[0:50]))]
print(data[0])
# print(data[0],data[1],data[2],data[3])
