from socket import *

# --server bilgileri-- 
# ifconfigden ip cek!
# server -> ip ve port
server = ("192.168.0.10", 5000)

# client socket tanimla
clientSocket = socket(AF_INET, SOCK_STREAM) # Tcp de SOCK_STREAM! Udp de SOCK_DGRAM!

clientSocket.connect(server) # connet TCP ye ozel 

# mesaji gonderilecek kullanicidan al
mssg = raw_input('>>>')

# mesaji server'a gonder 
# (11. satirda daha onceden server'la client socket arasinda baglanti kurulmustu zaten)
clientSocket.send(mssg) 

# server'dan donen data response'u al
data = clientSocket.recv(1024)
print "From server: ", data 

clientSocket.close()