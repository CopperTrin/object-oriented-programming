def count_minus(str):
    numbers = str.split()
    return sum(1 for num in numbers if int(num) < 0)


print(count_minus('10 20 30 -40 50 60'))