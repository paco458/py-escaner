import nmap
nm=nmap.PortScanner()
ip=input("Coloca tu ip: ")
nm.scan(hosts=ip, arguments="--top-ports 1000 -sV --version-intensity 3")
print("Comando ejecutado : {}".format(nm.command_line()))
print("Protocolo utilizados: {}".format(nm[ip].all_protocols()))
print("Estado de la maquina: {}".format(nm[ip].state()))
#print(nm[ip]["tcp"])
for puerto in nm[ip]["tcp"].keys():
    for data in nm[ip]["tcp"][puerto]:
        print(data + " : " + nm[ip]["tcp"][puerto][data])
