# Python program for removing i-th character from a string
s = input("Enter the String:")
i=int(input("Enter the index value:"))
for j in range(len(s)):
    if j == i:
        s = s.replace(s[i], "", 1)
print(s)
