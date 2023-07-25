import requests,sys



if len(sys.argv) != 2:
  print("****************************************************************************")
  print("*\t\t\t\t\t\t\t\t\t   *")
  print("*\t\t\t\t\t\t\t\t\t   *")
  print("*  SCRIPT FOR ENUMERATION OF ROBOTS.TXT AND SITEMAP.XML BY EWERTON FELIPE  *")
  print("*\t\t\t\t\t\t\t\t\t   *")
  print("*\t\t\t\t\t\t\t\t\t   *")
  print(f"*\t\tUsage: python3 {sys.argv[0]} <host>\t\t\t\t   *")
  print("*\t\t\t\t\t\t\t\t\t   *")
  print("*\t\t\t\t\t\t\t\t\t   *")
  print("****************************************************************************")
  
else:
	robots = f"http://{sys.argv[1]}/robots.txt"
	sitemap = f"http://{sys.argv[1]}/sitemap.xml"
	bots = requests.get(robots)
	smap = requests.get(sitemap)
	if bots.status_code == 200 and smap.status_code == 200:
		print("robots.txt exist and sitemap.xml exist")
	elif bots.status_code == 200:
		print("robots.txt exist")
	elif smap.status_code == 200:
		print("sitemap.xml exist")
	else:
		print("don't exist robots.txt or sitemap.xml")
