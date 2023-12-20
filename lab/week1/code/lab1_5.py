answer = 0
for first_num in range(1000):
    for second_num in range(1000):
        string = str(int(first_num * second_num))
        if string != string[::-1]:
            break
        elif answer < int(string):
            answer = int(string)

print(answer)
