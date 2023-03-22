number = [2, 4, 1, 5, 7, 10, 43, 23, 9, 8]

max_number = number[0]

for max in number:
    if max > max_number:
        max_number = max

print(max_number)