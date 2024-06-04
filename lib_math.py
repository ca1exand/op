import math
import argparse

# check if a given whole number is prime
def is_prime(n):
    if (n == 1):
        return 0
    elif (n == 2 or n == 3):
        return 1
    elif (n % 2 == 0):
        return 0
    elif (n < 9):
        return 1
    elif (n % 3 == 0):
        return 0
    else:
        r = math.floor(math.sqrt(n))
        for f in range(5, r, 6):
            if (n % f == 0):
                return 0
            if (n % (f + 2) == 0):
                return 0
        return 1

# check if a given whole number is coprime
def is_coprime(n):
    if (n>4 and is_prime(n)):
        if (is_prime(n+2) or is_prime(n-2)):
            return True
        else:
            return False
    elif (n==2 or n==3):
        return True
    else:
        return False

# return Fibonacci series up to n
def series_fibo(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


def sum_diagonal_spiral(l):
    s = 1
    c = 1
    a = 2
    for g in range(math.floor(l/2)):
        for i in range(1,5):
            c = c + a
            s = s + c
            print("new sum is " + str(s))
        a+=2
        print("new side length " + str(a))
    print("sum is " + str(s))

for i in range(1,10):
    print(i, "is prime:", is_prime(i))
    print(i, "is coprime:", is_coprime(i))

print(series_fibo(10))
print(sum_diagonal_spiral(1001))