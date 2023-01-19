import socket, sys


def pop_enum():
  ip = sys.argv[1]
  port = 110

  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((ip, port))
  #print(client)
  banner = client.recv(1024)
  print(banner)

  client.send(b"USER camila\r\n")
  client.send(b"PASS ca123456\r\n")

  user = client.recv(1024)
  passwd = client.recv(1024)

  print("USER")
  print(user)

  print("PASS")
  print(passwd)

  client.send(b"STAT\r\n")
  stat = client.recv(1024)
  print("STAT")
  print(stat)

  client.send(b"LIST\r\n")
  lista = client.recv(1024)
  print("LIST")
  print(lista)

  client.send(b"QUIT\r\n")
  quit = client.recv(1024)
  print("QUIT")
  print(quit)

  client.close()
  
if len(sys.argv) < 3:

  print(f"usage mode: python3 {sys.argv[0]} host 110")
  
else:
  pop_enum()
