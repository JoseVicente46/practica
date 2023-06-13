import random
random = random.randrange(0, 10)

num = int(input("Dime un numero del 0 al 10: "))

if num == random:
    print("Has adivinado el numero!!!")
else:
    while num != random:
        if num < random:
            num = int(input("El numero es menor que el random: "))
        else:
            num = int(input("El numero es mayor que el random: "))

    print("Has adivinado el numero!!!")