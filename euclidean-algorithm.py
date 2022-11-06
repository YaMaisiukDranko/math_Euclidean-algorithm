# @YaMaisiukDranko
# Euclidean Algorithm on Python

a = int(input("What's the first number? "))
b = int(input("What's the second number? "))

r=a%b

while r:
    a=b
    b=r
    r=a%b
    print("a:", a, "b:", b, "r:", r)
print('GCD is:', b)