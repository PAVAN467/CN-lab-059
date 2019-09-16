from socket import *
ServerName="172.17.0.1"
ServerPort=12002
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((ServerName,ServerPort))
serverSocket.listen(1)
print("the server is ready to receive")
while 1:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024).decode()
    file=open(sentence,"r")
    l=file.read(1024)
    connectionSocket.send(l.encode())
    file.close()
    connectionSocket.close()
    
