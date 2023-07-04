# Generating random strings until a given string is generated
import string
import random
s1 = input("enter the string:")
n = len(s1)
s2 = None
char = string.digits + string.ascii_uppercase + string.ascii_lowercase
c = 1
while s1 != s2:
    s2 = ''.join(random.choice(char) for i in range(n))
    c += 1
    print(c, s2)
    if s2 == s1:
        print("String matched after", c, "iterations")
