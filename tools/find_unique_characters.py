list = []
ignore = ["\u3000", "\n"]

for char in """

""":
    if char in list or char in ignore:
        pass
    else:
        list.append(char)

print()
print(list)
print()