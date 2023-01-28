import requests
import pyfiglet

banner = pyfiglet.figlet_format("File Downloader by Ewerton Felipe")
print(banner)

url = str(input("Enter the url: "))

f = str(input("Enter the file with extension: "))

mode_opened = str(input("Enter the mode: "))

r = requests.get(url, allow_redirects=True)
open(f, mode_opened).write(r.content)
