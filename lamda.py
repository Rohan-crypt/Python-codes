def recursive_sum(numbers, index=0):
    if index == len(numbers):
        return 0
    return numbers[index] + recursive_sum(numbers, index + 1)

numbers = [1, 2, 3, 4, 5]
total = recursive_sum(numbers)
print(total)