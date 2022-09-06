import socket


ports = [21, 22, 25, 80, 443, 8080, 3306] #porta 3306 eh do mysql

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex(("127.0.0.1", port))
    if code == 0:
        print("open port: " + str(port))
    else:
        print("closed port: " + str(port))
#client.send(b"hello world!") # O 'b' eh para transformar em bytes
#response = client.recv(1024) # recv recebe dados com um numero de bytes que queremos receber
#print(response.decode())
