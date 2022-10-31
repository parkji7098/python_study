import serial

PORT = "/dev/ttyUSB0"
BAUDRATE = 9600

# 시리얼 포트와 통신 준비
ser = serial.Serial(PORT, baudrate=BAUDRATE)

while True:
    # msg = 'q'
    msg = input()

    if (msg == '0'):
        break

    # print(f'input: {msg}')

    # 데이터를 전송, 보낸다, 쓴다
    ser.write(msg.encode())

ser.close()