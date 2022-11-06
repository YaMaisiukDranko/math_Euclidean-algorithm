# @YaMaisiukDranko
# Euclidean Algorithm on Python

import math

a = int(input("What's the first number? "))
b = int(input("What's the second number? "))

r=a%b

while r:
    #print("a:", a, "b:", b, "r:", r)
    digits = int(math.log10(a)) + 1
    print(a, "|" + "\033[4m", b, "\033[0m")
    print("  " * digits, int(a / b))
    a=b
    b=r
    r=a%b

digits = int(math.log10(a)) + 1
print(a, "|" + "\033[4m", b, "\033[0m")
print("  " * digits, int(a / b))
print('GCD is:', b)