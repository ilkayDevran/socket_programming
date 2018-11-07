from socket import *

# --server bilgileri-- 
# ifconfigden ip cek!
# server -> ip ve port
server = ("192.168.0.10", 5000)

# client socket tanimla ve server'a connect ol
clientSocket = socket(AF_INET, SOCK_DGRAM) # Udp de SOCK_DGRAM! Tcp de SOCK_STREAM! 

# mesaji gonderilecek kullanicidan al
mssg = raw_input('>>>')

# mesaji server'a gonder 
clientSocket.sendto(mssg, server)

# server'dan donen data response'u al
data, serverAddr = clientSocket.recvfrom(1024)
print "From server: ", data 

clientSocket.close()