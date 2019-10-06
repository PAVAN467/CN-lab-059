serverooo
----------------------
from socket import*



ServerName="192.168.56.1"
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
    a=l.split()
    print(len(a))
    connectionSocket.send(str(len(a)).encode())
    file.close()
    connectionSocket.close()
-----------------------------------------------------------------
from socket import *
clientName="192.168.56.1"
clientPort=12002
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((clientName,clientPort))
sentence=input("enter the file name")
clientSocket.send(sentence.encode())
filecontents=clientSocket.recv(1024).decode()
print('from server',filecontents)
clientSocket.close()
