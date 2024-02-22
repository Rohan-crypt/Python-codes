numbers = [10, 20, 5, 45, 60, 80]
largest = numbers[0]
for num in numbers[1:]:
    if num > largest:
        largest = num
print("The largest number in the list is:", largest)