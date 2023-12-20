input_line = input()
num = input_line.split()
num = [int(n) for n in num]


if int(input_line[0]) >= 7 and int(num[2]) <= 23 and int(num[0]) <= int(num[2]) and int(num[1]) < 60 and int(num[3]) < 60:
    hour = num[2] - num[0]
    minute = num[3] - num[1]
    time = (hour * 60) + minute
    cost = 0
    if time >= 360:
        cost = 200
    elif time > 180:
        time = time - 180
        cost = 30 + (-(-time//60) * 20)
    elif time > 15:
        cost = (-(-time//60) * 10)
    elif time <= 15:
        cost = 0
    print(cost)
else:
    print("ERROR")
