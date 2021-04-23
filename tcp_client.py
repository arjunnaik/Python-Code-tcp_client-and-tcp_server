from socket import *
serverName = 'localhost'
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input("input lowercase sentence")
clientSocket.send(message.encode())
modifiedSentence = clientSocket.recv(2048)
print(modifiedSentence.decode())
clientSocket.close()