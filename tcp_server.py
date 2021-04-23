from socket import *
serverPort = 9999
serverName = 'localhost'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(5)
print("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    print("Connected with client of address",addr)
    message = connectionSocket.recv(1024).decode()
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()