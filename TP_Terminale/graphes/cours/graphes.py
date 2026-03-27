m = [[0, 0, 1, 1, 0, 0, 0],
     [1, 0, 0, 0, 0, 1, 1],
     [1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 0],
     [0, 1, 0, 1, 0, 0, 0]]

def successeurs(m, l):
    return m[l]

def predecesseurs(m, c):
    liste = []
    for i in range(len(m)):
        liste.append(m[i][c])
    return liste

if __name__ == "__main__":
    print(str(successeurs(m, 0)))
    print(str(predecesseurs(m, 0)))