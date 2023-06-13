def ip_ok(ipf):
    num = 0
    pos = 0
    pospunt1 = 0
    pospunt2 = 0
    pospunt3 = 0
    pos3 = 0
    pos2 = 0
    pos1 = 0
    for i in ipf:
        if i.isdigit():
            num += 1
        elif i == "." and pos <= 3 and pospunt1 == 0:
            pospunt1 = "."
            pos1 = pos
        elif i == "." and pos <= 7 and pospunt2 == 0:
            pospunt2 = "."
            pos2 = pos
        elif i == "." and pos <= 11 and pospunt2 != 0 and pospunt3 == 0:
            pospunt3 = "."
            pos3 = pos
        else:
            return False
        pos += 1
    return 0 < len(ipf[:pos1]) <= 3 and 0 < len(ipf[pos1 +1 :pos2]) <= 3 and 0 < len(ipf[pos2 + 1:pos3]) <= 3 and 0 < len(ipf[pos3:-1]) <= 3 and len (ipf) > 5


ip = str(input("Dime el numero de tu IP(Para salir pon un 0): "))

while ip != 0:
    ip_ok(ip)
    print(ip_ok(ip))
    ip = str(input("Dime el numero de tu DNI(Para salir pon un 0): "))