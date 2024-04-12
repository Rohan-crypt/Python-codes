def min_max(list):
    min_value= filter(lambda x, y: x if x < y else y, list)
    max_value= filter(lambda x, y: x if x > y else y, list)
    return min_value,max_value