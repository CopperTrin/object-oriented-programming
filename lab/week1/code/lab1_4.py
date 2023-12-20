num = int(input())
list = []

if(num < 10):
    for i in range (1,5):
        list.append(int(str(num)*i))
        print(sum(list))
else:
    print("ERROR")

