# String
for ch in "Python":
    print(ch)

# Integer
for i in range(5):
    print(i)

# Enumerate
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

# Nested For
for i in range(3):
    for j in range(2):
        print(i, j)

# List
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)

# Dictionary
student = {"name": "John", "age": 22}
for key, value in student.items():
    print(key, ":", value)

# Tuple
for t in (1, 2, 3, 4):
    print(t)

# Zip()
names = ["A", "B", "C"]
marks = [80, 90, 85]
for n, m in zip(names, marks):
    print(n, m)
