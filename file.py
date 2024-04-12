a=open('typo.txt', 'r+')

a.write("hello\n")

b=open('1234.txt', 'w')

for data in a:
    b.write(data)