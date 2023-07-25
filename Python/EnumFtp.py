import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((ip,port))
banner = tcp.recv(1024)
print(f"BANNER: {banner}")
tcp.send(b"USER ftp\r\n")
user = tcp.recv(1024)
print(f"USER: {user}")
tcp.send(b"PASS ftp\r\n")
passw = tcp.recv(1024)

tcp.send(b"HELP\r\n")
tcp.send(b"PWD\r\n")
command = tcp.recv(2048)
print(f"{command}\r\n")

tcp.close()
