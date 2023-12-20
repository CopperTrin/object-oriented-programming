n = 10

for i in range(n * n):
    row = i // n
    col = i % n

    if row + col < n-1:
        print(' ', end="")
        
    else:
        print('#', end='')

    if col == n - 1:
        if(row != 9): print(' ', end="")
        print("")
        
       