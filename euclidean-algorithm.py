# @YaMaisiukDranko
# Euclidean Algorithm on Python

gcd = int
# Get a, b
a = int(input("Write a: "))
b = int(input("Write b: "))
print("GCD (", a, ";", b, ")")

if a % b != 0: #Check for 0
    print(a % b)
else:
    print(a / b)
