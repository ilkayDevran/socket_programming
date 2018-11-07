from socket import *

serverPort = 5000

# server icin socket tanimla ve bind et
serverSocket = socket(AF_INET, SOCK_STREAM) # Tcp de SOCK_STREAM! Udp de SOCK_DGRAM!
serverSocket.bind(("", serverPort))

serverSocket.listen(1) # listen TCP ye ozel!
print "Server Started!" 

while True:
    # gelen connection requestini kabul et
    connectionSocket, addr = serverSocket.accept() # accept TCP ye ozel
    # gelen data yi al
    mssg = connectionSocket.recv(1024)
    # gelen mesaji editleme kismi
    mssg = mssg.upper()
    # geri yolla
    connectionSocket.send(mssg)
    connectionSocket.close()

serverSocket.close()