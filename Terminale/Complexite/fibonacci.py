def fibonacci(n):
    if n <=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_all(n, l):
    if n <= 1:
        l[n] = n
        return n
    if l[n] != 0:
        return l[n]
    l[n] = fibonacci_all(n-1, l) + fibonacci_all(n-2, l)
    return l[n]

if __name__ == "__main__":
    n=50
    list = [0]*(n+1)
    print(fibonacci(n))
    print(fibonacci_all(n, list))
    print(list)