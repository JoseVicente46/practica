def ip_ok(ipf):
    vect = []
    vect = ipf.split(".")

    return len(vect[0]) < 4 and len(vect[1]) < 4 and len(vect[2]) < 4 and len(vect[3]) < 4


ip = str(input("Dime el numero de tu IP(Para salir pon un 0): "))

while ip != 0:
    print(ip_ok(ip))
    ip = str(input("Dime el numero de tu DNI(Para salir pon un 0): "))