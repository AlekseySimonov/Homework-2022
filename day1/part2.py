with open("input.txt") as f:
    n = f.read()
n =(list(n))
bkt = 0
number = 0
for i in n:
    if i == '(':
        bkt += 1
        number += 1
    if i == ')':
        bkt -= 1
        number += 1
    if bkt == -1:
        break
number = str(number)


output = open ('output2.txt', 'w')
output.write(number)

output.close()
f.close()

