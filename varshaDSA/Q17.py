list1 = [1, 3, 4, 5, 6, 7]
list2 = [5, 2, 8, 7, 1, 3]

common = list(set(list1) & set(list2))
print("Common elements:", common)
