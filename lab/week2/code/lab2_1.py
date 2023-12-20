input_line = input()
num = input_line.split()
zero_count = 0
num.sort()

for i in range(len(num)):
    if(num[i] == '0'):
        zero_count += 1
    else:
        print(num[i] + '0'*zero_count, end = '')
        zero_count = 0
        

