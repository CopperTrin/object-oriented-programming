def add2list(lst1, lst2):
    if(len(lst1) != len(lst2)): return -1
    else:return [x + y for x, y in zip(lst1, lst2)]

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(add2list(x, y))