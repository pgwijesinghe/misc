import serial
import time

t=0
ard = serial.Serial('com3',9600)
time.sleep(1)
print(ard.readline().decode('ascii'))
time.sleep(1)

ard.write(b'2870000000#2880000000#10#')

print(ard.readline().decode('ascii'))
print(ard.readline().decode('ascii'))
print(ard.readline().decode('ascii'))
 

ard.close()