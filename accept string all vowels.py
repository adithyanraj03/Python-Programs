str = input("Entre the string:")


def vow(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for char in string:
        if char not in vowels:
            print("string", str, "Not accepted")
            break
    else:
        print("string", str, "Accepted")


vow(str)
