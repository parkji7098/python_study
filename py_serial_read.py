import serial

PORT = "/dev/ttyUSB0" 
# PORT = "/dev/ttyUSB0" #리눅스, $ sudo chmod 666 /dev/ttyUSB0
BAUDRATE = 9600
# BAUDRATE = 115200

# 시리얼 포트와 통신 준비
ser = serial.Serial(PORT, baudrate=BAUDRATE)

while True:
    # 1.포트확인, 보드레이트*
    # 2.자료형, 인코딩

    # b'a'
    # readed = ser.read().decode(encoding='utf-8')
    # readed = ser.read().decode()

    line = ser.readline().decode().replace('\n', '')

    if line == 'q':
        break

    if line:
        # print("readed: ", readed, end="")
        print(line)

    # if readed == 'q':
    #     break

    # if readed:
    #     # print("readed: ", readed, end="")
    #     print(readed)

    pass

ser.close()