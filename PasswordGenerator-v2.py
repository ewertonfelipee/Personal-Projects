import string
import secrets

letters = string.ascii_letters
digits = string.digits

passwd_size = int(input("Password Size: "))

x = letters + digits

password = "".join(secrets.choice(x) for i in range(passwd_size)) # junta todos os elementos

print(password)
