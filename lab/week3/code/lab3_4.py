def char_count(s):
    dic_char_count = {}
    for alphabet in s:
        dic_char_count[alphabet] = s.count(alphabet)
    return dic_char_count

print(char_count('language'))