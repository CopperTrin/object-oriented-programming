def delete_minus(list):
    result = [[num for num in sub_list if num >= 0] for sub_list in list]
    return result

x = [ [1, -3, 2], [-8, 5], [-1, -4, -3] ]
print(delete_minus(x))