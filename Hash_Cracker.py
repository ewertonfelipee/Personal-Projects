import hashlib
import pyfiglet


banner = pyfiglet.figlet_format("Hash Cracker by Ewerton Felipe")
print(banner)

worldlist_location = str(input('Enter wordlist location: '))
hash_input = str(input('Enter the hash: '))

with open(worldlist_location, 'r') as f:
  for line in f.readlines():
    hash_ob = hashlib.sha256(line.strip().encode())
    hashed_pass = hash_ob.hexdigest()
    if hashed_pass == hash_input:
      print('Found cleartext password! ' + line.strip())
      exit(0)
