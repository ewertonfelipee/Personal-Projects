import dns.resolver

res = dns.resolver.Resolver()
file = open("/file/path/", "r")
for subdomain in file.read().splitlines():

    target = subdomain + ".URL"

    try:
        result = res.resolve(target, "A")
        for ip in result:
            print(target ,"->", ip)
    except:
        pass #pass nao mostra nada na tela
        
file.close()
