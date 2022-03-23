input = open('input.txt', 'r')
total = 0
while True:
    box = input.readline()
    box = box.replace('x', ' ')
    a = list(map(int, box.split()))
    a = sorted(a)
    for i in range (len(a)):
        l = a[0]
        h = a[1]
        w = a[2]

        paper = 2 * h + 2 * l + w * l * h

    if not box:
        break

    total += paper
print(total)

output = open('output2.txt', 'w')
output.write(str(total))

output.close()
input.close()