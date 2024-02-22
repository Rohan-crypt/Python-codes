# WAP to remove dublicate from a list
list=[2,4,5,5,4,6,10,6]
list2=[]
for num in list:
        if num not in list2:
            list2.append(num)
print(list2)