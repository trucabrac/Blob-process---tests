import serial
import datetime
from datetime import datetime
import time

arduino_port = "COM3" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName="analog-data.csv" #name of the CSV file generated

ser = serial.Serial(arduino_port, baud)
#print("Connected to Arduino port:" + arduino_port)
file = open(fileName, "a")
#print("Created file")

samples = 1000 #how many samples to collect
print_labels = False
line = 0 #start at 0 because our header is 0 (not real data)
while line <= samples:
    # incoming = ser.read(9999)
    # if len(incoming) > 0:
    
    val = ser.readline()
    if val:
        now = datetime.now()
        timestamp = str(int(datetime.timestamp(now)))
        string = val.decode()  # convert the byte string to a unicode string
        #num = int(string) # convert the unicode string to an int
        data = str(timestamp + ',' + string)
        print(data)
    
    #getData=str(ser.readline())
    #data=getData[0:][:-1]
    #print(data)

        file = open(fileName, "a")
        file.write(data) #write data with a newline
        line = line+1
    
        #time.sleep(1)

print("Data collection complete!")
file.close()
ser.close()