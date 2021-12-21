def factoriel(n):
    if(n == 0 or n == 1):
        return 1
    return n * factoriel(n -1)

print(factoriel(4))

def fibonacci(n):
    #f de n = f de n -1 + f de n -2
     # f de 0 = 0 et f de 1 = 1
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fibonacci(n -1) + fibonacci(n - 2)

print(fibonacci(4))

#fibonacci(4) = fibonacci(3) + fibonacci(2) = (fibonacci(2) + fibonacci(1)) + (fibonacci(1) + fibonacci(0)) = ((fibonacci(1) + fibonacci(0)) + fibonacci(1)) + (fibonacci(1) + fibonacci(0)) = 1 + 0 + 1 + 1 +0
#fibonacci(3) = fibonacci(2) + fibonacci(1)
#fibonacci(2) = fibonacci(1) + fibonacci(0)
#fibonacci(1) = 1

    