input = open('input.txt', 'r')
total = 0
while True:
    box = input.readline()
    box = box.replace('x', ' ')
    a = list(map(int, box.split()))
    for i in range (len(a)):
        l = a[0]
        h = a[1]
        w = a[2]
    paper = 2*l*h+2*h*w+2*w*l+min(l*h,h*w,w*l)
    if not box:
        break

    total += paper
print(total)

output = open('output1.txt', 'w')
output.write(str(total))

output.close()
input.close()