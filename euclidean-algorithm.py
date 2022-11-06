# @YaMaisiukDranko
# Euclidean Algorithm on Python

a = int(input("What's the first number? "))
b = int(input("What's the second number? "))

r=a%b

while r:
    print("a:", a, "b:", b, "r:", r)
    a=b
    b=r
    r=a%b

print('GCD is:', b)