import timeit

def somme1(n):
    return n*(n+1)/2

def somme2(n):
    s=0
    for i in range(1, n+1):
       s+=i
    return s

def somme_rec(n):
    if n==1:
        return n
    return n + somme_rec(n-1)

def somme_suite_geo1(n, q):
    return (1-q**n)/(1-q)

def somme_suite_geo2(n, q):
    s=0
    t=1
    for i in range(1, n+1):
        s+=t
        t*=q
    return s

def somme_suite_rec(n, q):
    if n==0:
        return n
    return q**(n-1) + somme_suite_rec(n-1,q)

print("Somme des factoriel : ")
starttime1 = timeit.default_timer()
for i in range(10000):
    somme1(10)
print("La différence de temps est pour somme1 :", timeit.default_timer() - starttime1)
starttime2 = timeit.default_timer()
for i in range(10000):
    somme2(10)
print("La différence de temps est pour somme2 :", timeit.default_timer() - starttime2)
starttime3 = timeit.default_timer()
for i in range(10000):
    somme_rec(10)
print("La différence de temps est pour somme_rec :", timeit.default_timer() - starttime3)
print()
print("Somme des suites géométriques : ")
starttime4 = timeit.default_timer()
for i in range(10000):
    somme_suite_geo1(10, 2)
print("La différence de temps est pour somme_suite_geo1 :", timeit.default_timer() - starttime4)
starttime5 = timeit.default_timer()
for i in range(10000):
    somme_suite_geo2(10, 2)
print("La différence de temps est pour somme_suite_geo2 :", timeit.default_timer() - starttime5)
starttime6 = timeit.default_timer()
for i in range(10000):
    somme_suite_rec(10, 2)
print("La différence de temps est pour somme_suite_rec :", timeit.default_timer() - starttime6)