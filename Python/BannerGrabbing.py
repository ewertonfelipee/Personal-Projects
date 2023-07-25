import socket
import sys

try:
  ip = sys.argv[1]
  port = int(sys.argv[2])
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect_ex((ip, port))
  banner = client.recv(1024)
  print(banner)
except:
  if(len(sys.argv) < 3):
    print("BANNER GRABBING - EWERTON FELIPE")
    print("Usage Example: python3 program.py target port")
  else:
    pass
