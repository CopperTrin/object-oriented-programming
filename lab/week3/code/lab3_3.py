def is_plusone_dictionary(d):
    list = [item for pair in d.items() for item in pair]
    for i in range(len(list)-1):
          if list[i] != list[i+1]-1:
                return False
    return True
