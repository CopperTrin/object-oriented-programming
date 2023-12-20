def count_char_in_string(x,c):
    return [string.count(c) for string in x]
    

x = ['abba', 'babana', 'ann']
c = 'a'
print(count_char_in_string(x,c))