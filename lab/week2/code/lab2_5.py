def only_english(string1):
    return "".join(char for char in string1 if char.isalpha())

input_line = input()
print(only_english(input_line))