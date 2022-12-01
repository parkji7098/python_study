import socket

# HOST = '127.0.0.1'
HOST = '192.168.0.36'
PORT = 9999

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))

while True:
    inputText = input('send message: ')

    clientSocket.send(inputText.encode())

    data = clientSocket.recv(1024)
    print('Received message: ', data.decode())