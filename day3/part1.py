input = open('input.txt','r')
input_list = list(input)
direction = sum([list(i) for i in input_list], [])

x = 0
y = 0
N_S = []
W_E = []

for i in direction:
    if i == '<':
        y -= 1
        N_S.append(x)
        W_E.append(y)
    elif i == '>':
        y += 1
        N_S.append(x)
        W_E.append(y)
    elif i == '^':
        x += 1
        N_S.append(x)
        W_E.append(y)
    elif i == 'v':
        x -= 1
        N_S.append(x)
        W_E.append(y)

result = len(set([' '.join(str(x)) for x in zip(N_S, W_E)]))

output = open('output1.txt', 'w')
output.write(str(result))

output.close()
input.close()



