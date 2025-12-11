# String
for ch in "Python":
    print(ch)

# Integer range
for i in range(5):
    print(i)

# Enumerate
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

# List
lst = [10, 20, 30]
for x in lst:
    print(x)

# Nested for
for i in range(2):
    for j in range(3):
        print(i, j)

# Dictionary
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)

# Tuple
t = (1, 2, 3)
for x in t:
    print(x)

# Zip
names = ["John", "Sara"]
marks = [90, 85]
for n, m in zip(names, marks):
    print(n, m)
