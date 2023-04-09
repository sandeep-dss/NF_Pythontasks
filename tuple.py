tuple = ("hi", False, 1, 1, 1, 2.5)
print(tuple)

for i in tuple:
    if tuple.count(i) > 1:
        print(i)