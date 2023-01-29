import requests 
import sys 
import pyfiglet

banner = pyfiglet.figlet_format("Directory enumerator by PR0.XY")
print(banner)

wordlist = str(input("Enter with the wordlist path: "))

sub_list = open(wordlist).read() 

directories = sub_list.splitlines()

url = str(input("Enter with the URL: "))

extension = str(input("Enter with the extension of wordlist directories: "))

for dir in directories:

    dir_enum = f"http://{url}/{dir}.{extension}" 

    r = requests.get(dir_enum)

    if r.status_code==404: 

        pass

    else:

        print("Valid directory:", dir_enum)
