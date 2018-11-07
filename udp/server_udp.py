from socket import *

serverPort = 5000

serverSocket = socket(AF_INET, SOCK_DGRAM) # Udp de SOCK_DGRAM! Tcp de SOCK_STREAM! 
serverSocket.bind(("", serverPort))
print "Server Started!"

while True:
    mssg, addr = serverSocket.recvfrom(1024)
    # gelen mesaji editleme kismi
    mssg = mssg.upper()
    # geri yolla
    serverSocket.sendto(mssg, addr)

serverSocket.close()