for i in range(1, 6):
    if i == 2:
        continue  # skip 2
    elif i == 4:
        break     # stop at 4
    elif i == 3:
        pass      # do nothing
    print(i)
else:
    print("Loop completed")
