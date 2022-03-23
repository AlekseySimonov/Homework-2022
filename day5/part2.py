input = open('input.txt','r')
total = 0

def Iteration(string):
    iteration = 0
    for x, y in zip(string[0:], string[1:]):
        s = ''.join(x+y)
        print(s)
        if string.count(x+y) >= 2:
            iteration += 1
    return iteration

def Between(string):
    double = 0
    for x, z in zip(string[0:], string[2:]):
        if x == z:
            double += 1
    return double

i = 0
while i <= 1000:
    string = input.readline()
    iteration = Iteration(string)
    doubles = Between(string)
    if doubles >= 1 and iteration >= 1:
        total += 1
    i += 1

output = open('output2.txt', 'w')
output.write(str(total))

output.close()
input.close()