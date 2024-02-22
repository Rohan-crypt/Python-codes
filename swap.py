# WAP to swap first and last element of the list
lst = [1, 2, 3, 4, 5,6,7,8,9,10]
print("Original list:", lst)
if len(lst) < 2:
        print("The list must have at least two elements.")
else:
    lst[0], lst[-1] = lst[-1], lst[0]
    print("List after swapping first and last elements:", lst)