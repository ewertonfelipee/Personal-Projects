import requests
import sys

robots = f"http://{sys.argv[1]}/robots.txt"
sitemap = f"http://{sys.argv[1]}/sitemap.xml"
bots = requests.get(robots)
smap = requests.get(sitemap)
if bots.status_code == 200 or smap.status_code == 200:
  print("robots.txt or sitemap.xml exist")
else:
  print("don't exist robots.txt or sitemap.xml")
