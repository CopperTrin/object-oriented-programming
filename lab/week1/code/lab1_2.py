upper = 0
lower = 0
input_str = str(input(""))

for i in range(len(input_str)):
    if input_str[i].isupper():
        x += 1
    elif input_str[i].islower():
        y += 1

print("Number of uppercase letters:", x)
print("Number of lowercase letters:", y)