import random


# Use list and dictunary comprehensions

mixed = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
print("Initial list of players:", mixed)
# upper_all = [name.upper() for name in mixed]
upper_all = []
for name in mixed:
    if name.islower():
        upper_all.append(name.capitalize())
    else:
        upper_all.append(name)
print("New list with all names capitalized: ",upper_all)
upper_only = [name for name in mixed if name[0].isupper()]
print("New list of capitalized names only:", upper_only)