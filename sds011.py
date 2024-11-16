import serial
# conectar mq135 ao gpio
ser = serial.Serial('/dev/ttyUSB0')  # porta
data = ser.read(10)  # envia pacotes de 10 bytes
pm2_5 = int.from_bytes(data[2:4], byteorder='little') / 10  # converte os dados
