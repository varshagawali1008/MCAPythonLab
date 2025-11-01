# Example: Create a dictionary of squares
squares = {x: x**2 for x in range(5)}
print(squares)

# Example: List comprehension from dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict_comp = {k: v for k, v in zip(keys, values)}
print(dict_comp)
