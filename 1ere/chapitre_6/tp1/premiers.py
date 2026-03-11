def estpremier(entier):
    for n in range(2,entier):
        if entier%n == 0:
            return False
    return True

def premier(n):
    t = []
    indice=0
    nombre=2
    while len(t)<n:
        for i in range(2,)
        if estpremier(nombre)==True:
            t.append(indice)
            indice+=1
        nombre+=1
    return t

if __name__ == "__main__":
    print(premier(50))