import socket
import sys

#ports = [21, 22, 25, 80, 443, 8080, 3306] #porta 3306 eh do mysql
ip = sys.argv[1]

for port in range(1,1000):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex((ip, port))
    if code == 0:
        print("open port: " + str(port))
    else:
        pass
#client.send(b"hello world!") # O 'b' eh para transformar em bytes
#response = client.recv(1024) # recv recebe dados com um numero de bytes que queremos receber
#print(response.decode())
