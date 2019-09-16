from socket import *

clientName="172.17.0.1"
clientPort=12002
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((clientName,clientPort))
sentence=input("enter the file name")
clientSocket.send(sentence.encode())
filecontents=clientSocket.recv(1024).decode()
print('from server',filecontents)
clientSocket.close()
