import random
random = random.randrange(0, 10)

num = int(input("Dime un numero del 0 al 10: "))
print(random)
if num == random:
    print("Has adivinado el numero!!!")
else:
    while num != random:
        if num < random:
            num = int(input("No as acertado el numero es menor que el random: "))
        else:
            num = int(input("No as acertado el numero es mayor que el random: "))

    print("Has adivinado el numero!!!")