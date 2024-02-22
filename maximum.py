def maxval(a):
    max=a[0]
    for i in a:
        if (max<i):
            max=i
    return max
a=[10,20,22,28,36,41,12,11,9,27,91]
no=maxval(a)
print("Maxvalue in the list is ", no)