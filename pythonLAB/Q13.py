# Loop manipulation using pass, continue, break and else

for i in range(1, 10):
    if i == 2:
        pass  # Does nothing, just a placeholder
    if i == 5:
        continue  # Skips the value 5
    if i == 8:
        break  # Loop stops when i = 8
    print(i)
else:
    print("Loop completed successfully")
