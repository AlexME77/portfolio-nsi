import random

solution = random.randint(1, 100)
nombre = -1
tentative = 0

while nombre != solution:
    nombre = int(input("Saisir un nombre de 0 à 100 : "))
    tentative  += 1
    message = ""
    if nombre > solution:
        message = "Plus petit"
    elif nombre < solution:
        message = "Plus grand"
    if message:
        distance = abs(nombre - solution)
        if distance <= 2:
            message += ", tu brûles !"
        elif distance <= 10:
            message += ", tu chauffes !"
        print(message)

print("Bravo, la solution est bien",solution,", tu as trouvé en", tentative, "tentatives")