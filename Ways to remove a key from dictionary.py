# Different ways to remove key from dictionary
d = {"a": 10, "b": 20, "c": 30, "d": 40}
print("The dictionary : ", str(d))
print("Using del to remove a dict :")
# Using del to remove a dict
del d['b']
print("New dictionary after removal using del command is : ", str(d))
# Using pop() to remove a dict
print("\n")
print("The dictionary : ", str(d))
print("Using pop() to remove a dict :")
removed_value = d.pop('d')
print("New dictionary after removal using pop command is : ", str(d))
