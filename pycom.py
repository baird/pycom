import serial

connected = False

ser = serial.Serial("/dev/tty.usbmodem411", 9600)

## loop

while not connected:
    serin = ser.read()
    connected = True

ser.write("1")

## done

while ser.read() == '1':
    ser.read()
    ser.close()