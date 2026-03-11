temp = int(input("Quelle est la température de l'eau ?"))
if temp>=100:
    print("L'eau est à l'état gazeux")
elif temp<=0:
    print("L'eau est à 'état solide")
else:
    print("L'eau est à l'état liquide")
