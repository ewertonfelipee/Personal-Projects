import requests
import sys

robots = f"{sys.argv[1]}://{sys.argv[2]}/robots.txt"
bots = requests.get(robots)
if bots.status_code == 200:
  print("robots.txt exists")
else:
  print("don't exist")
