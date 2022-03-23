with open("input.txt") as number:
    a = number.read()

a =(list(a))
j = 0
for i in a:
    if i == ')':
        j += -1
    elif i == '(':
        j += 1

i = str(j)

output = open ('output1.txt', 'w')
output.write(i)

output.close()
number.close()
