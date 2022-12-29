import random
import string 

upper = string.ascii_uppercase
lower = string.ascii_lowercase
symbols = string.punctuation
digits = string.digits

all = upper + lower + symbols + digits

length = 16

password = "".join(random.sample(all, length))

print(password)
